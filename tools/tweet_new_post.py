# Post to Twitter
import os
import glob
import re
import sys
import frontmatter
import tweepy
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Twitter API credentials
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

def get_twitter_client():
    """Get authenticated Twitter Client (API v2)"""
    if not all([CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
        print("Error: Twitter API credentials not found in .env file.")
        sys.exit(1)
        
    return tweepy.Client(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

def get_latest_post():
    """Find the most recently modified markdown file in _posts directories"""
    search_paths = [
        "jp/_posts/*.md",
        "en/_posts/*.md"
    ]
    
    files = []
    for path in search_paths:
        files.extend(glob.glob(path))
        
    if not files:
        return None
        
    # Sort by modification time, newest first
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

def parse_post(file_path):
    """Parse markdown post to extract title, date, and build URL"""
    post = frontmatter.load(file_path)
    
    # Extract date and title from filename if not in frontmatter
    # Filename format: YYYY-MM-DD-title.md
    filename = os.path.basename(file_path)
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})-(.+)\.md', filename)
    
    if match:
        date_str = f"{match.group(1)}/{match.group(2)}/{match.group(3)}"
        slug = match.group(4)
    else:
        # Fallback if filename doesn't match standard Jekyll format
        print(f"Warning: Could not parse filename format: {filename}")
        return None

    # Determine language from directory
    lang = "jp" if "jp/_posts" in file_path else "en"
    
    # Build URL (assuming default Jekyll permalink structure: /lang/year/month/day/slug.html)
    # Check _config.yml for permalink structure if needed. 
    # Current assumption: /:lang/:categories/:year/:month/:day/:title.html
    # But based on directory structure (jp/_posts), likely /jp/yyyy/mm/dd/title.html
    
    # Note: Using slug from filename is safer than title which might contain spaces/special chars
    url = f"https://mdaisuke.net/{lang}/{date_str}/{slug}/"
    
    return {
        "title": post.get("title", slug),
        "excerpt": post.get("excerpt", ""),
        "url": url,
        "lang": lang,
        "path": file_path
    }

def main():
    print("--- Auto Tweet Script ---")
    
    # 1. Get latest post
    latest_file = get_latest_post()
    if not latest_file:
        print("No posts found.")
        return

    print(f"Latest post found: {latest_file}")
    
    # 2. Parse post info
    post_data = parse_post(latest_file)
    if not post_data:
        print("Failed to parse post data.")
        return
        
    print(f"Title: {post_data['title']}")
    print(f"URL: {post_data['url']}")
    
    # 3. Confirm tweet content
    tweet_text = f"New post: {post_data['title']}\n\n{post_data['excerpt']}\n\n{post_data['url']}"
    
    # Simple localization
    if post_data['lang'] == 'jp':
        tweet_text = f"ブログを更新しました: {post_data['title']}\n\n{post_data['excerpt']}\n\n{post_data['url']}"
    
    print("\n------------------------------------------------")
    print(tweet_text)
    print("------------------------------------------------\n")
    
    confirm = input("Post this tweet? (y/n): ").lower()
    if confirm != 'y':
        print("Cancelled.")
        return

    # 4. Post to Twitter
    try:
        client = get_twitter_client()
        response = client.create_tweet(text=tweet_text)
        print(f"Successfully posted! Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    main()

