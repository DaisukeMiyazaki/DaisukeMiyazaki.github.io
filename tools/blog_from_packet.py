import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING = ROOT / "staging"
POSTS = ROOT / "jp" / "_posts"
PACKET_VERSION = 1

def die(message):
    """stop without writing anything"""
    print(f"{message}")
    sys.exit(1)

def enc(name):
    """Encode spaces only, matching how existing posts reference assets"""
    return name.replace(" ", "%20")

def yaml_str(value):
    """Quote a value for a YAML front matter scalar"""
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'

def list_packets():
    """print the packets waiting in staging/"""
    dirs = [d for d in STAGING.iterdir() if d.is_dir() and d.name != "done"] if STAGING.exists() else []
    if not dirs:
        die("statingにpackektがありません")
    print("転写できるpacket:")
    for d in sorted(dirs):
        meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
        print(f"  {d.name}\t{meta['title']}\t(exported {meta['exportedAt'][:10]})")
    print("\n  python tools/blog_from_packet.py <slug>")

def load_packet(slug):
    """read and validate the packet. Any violoation stops the run"""
    d = STAGING / slug
    if not d.exists():
        die(f"packetがありません: staging/{slug}")

    meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
    if meta.get("packetVersion") != PACKET_VERSION:
        die(f"packetVersion {meta.get('packetVersion')} は未対応（対応するのは {PACKET_VERSION}）")
    for key in ("slug", "title", "created", "exportedAt", "attachments", "links"):
        if key not in meta:
            die(f"meta.jsonに {key} がありません")
    if meta["slug"] != slug:
        die(f"meta.json の slug ({meta['slug']}) がディレクトリ名と違います")
    for a in meta["attachments"]:
        if not (d / "attachments" / a["file"].exists()):
            die(f"添付が見つかりません: {a['file']}")
    if any(re.sub(r"^\d{4}-\d{2}-\d{2}-", "", f.name) == f"{slug}.md" for f in POSTS.iterdir()):
        die("同じslugの記事がすでにあります")

    return d, meta


def transform(body, slug):
    """rewrite image paths, demote h1, and resolve blogref markers"""
    body = re.sub(
        r"\]\(attachments/([^)]+)\)",
        lambda m: f"](/assets/images/{slug}/{enc(m.group(1))})",
        body,
    )
    # the layout renders the title, so a body h1 would duplicate it
    body = re.sub(r"^# (?=\S)", "## ", body, flags=re.MULTILINE)

    existing = [f.name for f in POSTS.iterdir() if f.suffix == ".md"]
    resolved, dropped = [], []

    def resolve(m):
        text, target = m.group(1), m.group(2)
        found = next((n for n in existing if n == "f{target}.md" or n.endswith("f-{target}.md")), None)
        date_part = re.match(r"^(\d{4})-(\d{2})-(\d{2})-", found or "")
        if not date_part:
            dropped.append(target)
            return text
        resolved.append(target)
        y, mo, d = date_part.groups()
        return f"[{text}](/jp/{y}/{mo}/{d}/{target}/)"

    body = re.sub(r"\[([^\]]*)\]\(blogref:([^)]+)\)", resolve, body)
    if "](blogref:" in body:
        die("blogref マーカーが解決できずに残りました")

    return body, resolved, dropped

def make_excerpt(body, limit=120):
    """take first 120 characters of prose, skipping heading and quotes"""
    lines = [
        re.sub(r"^\s*[-*+]\s+", "", line)
        for line in body.split("\n")
        if line.strip() and not re.match(r"^\s*[#>|]", line)
    ]
    plain = "".join(lines)
    plain = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", plain)
    plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", plain)
    plain = re.sub(r"[*`]", "", plain).strip()
    return plain[:limit] + "…" if len(plain) > limit else plain


def build_post(meta, date, body, slug):
    """Assemble the front matter and body"""
    attachments = meta["attachments"]
    thumbnail = f"/assets/images/{slug}/{enc(attachments[0]['file'])}" if attachments else ""
    return (
        "---\n"
        "layout: post\n"
        f"date: {date}\n"
        f"title: {yaml_str(meta['title'])}\n"
        f"excerpt: {yaml_str(make_excerpt(body))}\n"
        "comments: true\n"
        "lang: jp\n"
        f"lang-ref: {slug}\n"
        "genre: 実用\n"
        f"thumbnail: {thumbnail}\n"
        "---\n\n"
        f"{body.strip()}\n"
    )


def publish(packet_dir, meta, slug, date, post):
    """write the draft, move the images, and retire the packet"""
    if meta["attachments"]:
        img_dir = ROOT / "assets" / "images" / slug
        img_dir.mkdir(parents=True, exist_ok=True)
        for a in meta["attachments"]:
            shutil.copy2(packet_dir / "attachments" / a["file"], img_dir / a["file"])

    name = f"{date}-{slug}.md"
    (POSTS/ name).write_text(post, encoding="utf-8")

    # attachments live in assets/ so the reired packet does not keep them
    done_dir = STAGING / "done" / slug
    done_dir.mkdir(parents=True, exist_ok=True)
    meta["published"] = {
        "date": date,
        "jp": f"jp/_posts/{name}",
        "transcribedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    (done_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    shutil.move(str(packet_dir/ "note.md"), str(done_dir / "note.md"))
    shutil.rmtree(packet_dir)
    return name

def main():
    parser = argparse.ArgumentParser(description="packetを jp/_postsの下書きに転写する")
    parser.add_argument("slug", nargs="?", help="省略するとstagingの候補を並べる")
    parser.add_argument("--dry", action="store_true", help="書かずに出力を表示する")
    args = parser.parse_args()

    if not args.slug:
        list_packets()
        return

    packet_dir, meta = load_packet(args.slug)
    date = datetime.fromisoformat(meta["exportedAt"].replace("Z", "+00:00")).astimezone().strftime("%Y-%m-%d")

    body = (packet_dir / "note.md").read_text(encoding="utf-8")
    body, resolved, dropped = transform(body, args.slug)
    if len(resolved) + len(dropped) != sum(l["occurrences"] for l in meta["links"]):
        die("マーカーの件数がmeta.jsonのlinksと合いません")

    post = build_post(meta, date, body, args.slug)
    if args.dry:
        print(post)
        return

    name = publish(packet_dir, meta, args.slug, date, post)
    print(f"✓  jp/_posts/{name}")
    if meta["attachments"]:
        print(f"  画像 {len(meta['attachments'])} 枚 → assets/images/{args.slug}/")
    if resolved:
        print(f"  リンク解決 {len(resolved)} 件")
    if dropped:
        print(f"  リンクを外した: {', '.join(sorted(set(dropped)))}（該当記事が未転写）")
    print(f"  packet → staging/done/{args.slug}/")

if __name__ == "__main__":
    main()