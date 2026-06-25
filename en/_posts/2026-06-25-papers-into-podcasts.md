---
layout: post
date: 2026-06-25
title: "I Want to Listen to My Unread Papers, Not Read Them — and the Auto-Podcast Wasn't Enough"
excerpt: "Auto-generated podcasts turn any text into natural-sounding audio, but they're thin on examples and ask no real questions. So I built a pipeline that digests a paper with concrete examples and an interviewer-grade questioner — as an on-ramp to the primary source, not a replacement for it."
comments: true
lang: en
lang-ref: papers-into-podcasts
genre: practical
thumbnail:
---

## The papers I'm curious about but never sit down to read

I keep running into papers and long essays I'm genuinely curious about. The curiosity is real; the focus to sit down and read them is not. Reading is active work, and I rarely find the slot for it.

The time I *do* have is the passive kind — a commute, a walk, the few minutes I spend staring out a window. That time arrives whether I plan for it or not, and for this kind of material those moments are actually the best ones: listening slots into them in a way reading never will. So what I want isn't a summary to skim or a transcript. I want the thing broken down plainly enough that it comes in just by listening, hands free.

## NotebookLM and the auto-podcast almost solve this

Google's existing tools already do most of this. NotebookLM's Audio Overview, and the audio in Deep Research, turn a pile of text into a natural, podcast-style conversation between two hosts. For a daily listen, for gathering information, for buying back the reading time I never have, it's genuinely good — the voices sound human and the tone lands.

After a while, though, the limit shows. The examples are thin, and I can't control the length. It explains, but it doesn't make the thing click, and it isn't always comprehensive. Next to a real podcast — where a good host pulls a vivid, specific example out of a guest — the auto version feels flat. It tells you what the paper says without ever making it land.

## So I built the part the auto-podcast skips

Two things the generic version is weak on: examples and questions. Those are the parts I built up. The script is split into two roles.

**The explainer's real job is to translate.** Every abstract claim has to come with a concrete example or an analogy. If a term shows up, it gets unpacked on the spot. No bare jargon survives.

**The questioner is the listener's proxy.** I studied a list of the "ten best podcast interviewers"[^interviewers] and read what each says about their craft, then deliberately pulled out only the hard skills that move comprehension forward: ask short questions, follow up on the thing just said, voice the exact place a listener gets stuck, push past breadth toward the crux, and demand an example. The soft skills — warmth, rapport, humor itself — I dropped on purpose, because in this context they add noise to the script, and when you're working with an agent they invite hallucination.

The pipeline itself is plain: take a PDF, extract it, map its logic, digest it into plain language *with examples*, budget the length to 15–30 minutes, write the two-voice dialogue, and verify it against the source. Then [Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/speech-generation) gives it a natural voice — the one part the auto-podcast already nails, so I let the machine keep doing it.

The TTS step is just a small script — voices fixed, paced, and chunked to fit the model's limits: [gemini_tts.py](https://gist.github.com/DaisukeMiyazaki/5fb8e0333d7fe940aa9262b4d790eeb2).

## Where it went wrong

Early on I used gemini-2.5, and the tempo was too fast — *tonton-byoushi*, the two voices volleying without a breath between them. It sounded efficient and felt exhausting. The fix was small: pauses between turns, a calmer delivery, a director's note telling the model not to rush. What it taught me wasn't small, though — it needs *ma*, room to breathe.

What surprised me: Gemini 3.1 Flash TTS supplies those pauses and that speaking tone — the parts that look a lot like soft skills — on the model's side. Listening to 2.5 and 3.1 back to back, the difference was obvious.

## Wrapping up

The job of this tool is to digest things down so I'll actually *touch the primary source* I'd otherwise never open. The audio is an on-ramp to the paper, not a substitute for it. For something I just want to be aware of, it gets me far further than reading a summary would. But for a paper that snags me, I don't stop at listening — I go to the source and digest it in my own words. That digestion is the part I have to do myself. As I wrote in [the walking piece](/en/2025/09/17/sanpou-issue/), the first-hand insight AI can't generate for you only comes from there.

This tool has its limits, too: even after it writes a script and I ask it for examples, some things still don't click. For those, I ask the agent in my own words — not from a template — keeping the paper itself in context, and in my case having it sketch a diagram when that helps. Then I write the resolution into Obsidian. It's slow, but clearing them one at a time is how a paper I only listened to slowly becomes my own. [We must not delegate understanding](/en/2025/07/03/we-must-not-delegate-understanding/).

A note on rights: I'm not publishing the generated audio — or the script it's read from — here. The audio is just the script spoken aloud, so both are the same derivative work. I'd rather not distribute a derivative of someone else's paper without the rightsholder's permission, so I keep it to my own personal use — and if you run the same setup, please keep it to material you've legitimately obtained, for your own use.

[^interviewers]: Source: Frank Racioppi, "[The Ten Best Interviewers In Podcasting](https://podalization.substack.com/p/the-ten-best-interviewers-in-podcasting)" (Ear Worthy / Pod-Alization, 2023). Starting from this article, I dug into each host's own statements, blogs, and interviews. Primary sources, per host: [Michael Barbaro](https://www.pressclubinstitute.org/2020/07/20/terry-gross-and-michael-barbaro-share-interview-tips-and-techniques/), [David Pogue](https://pogueman.substack.com/p/pogues-top-ten-interview-tips), [Audie Cornish](https://www.cjr.org/special_report/qa-nprs-audie-cornish-on-the-intimacy-of-interviewing.php), [Elaine Appleton Grant](https://soundjudgment.substack.com/p/interviews-are-the-foundation-of), [Robert Peterpaul](https://vocal.media/interview/the-art-of-kindness-podcast-a332g0iko), [Mike Carruthers](https://www.somethingyoushouldknow.net/about/), [Evan Stern](https://tinkmedia.co/interviews/evan-stern), [Matt Gilhooly](https://veritysangan.com/podcast-archive/ep-58-getting-curious-and-hosting-amazing-guest-interviews-with-matt-gilhooly/), [Jordan Harbinger](https://www.podcastjunkies.com/jordan-harbinger-interview-2/), [Zale Mednick](https://booktime584.wordpress.com/2023/04/04/preconceivedinterview/).
