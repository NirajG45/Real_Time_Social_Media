from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_youtube_trending():
    youtube = build("youtube", "v3", developerKey=API_KEY)
    req = youtube.videos().list(part="snippet", chart="mostPopular", maxResults=5, regionCode="IN")
    res = req.execute()

    return [{
        "title": item["snippet"]["title"],
        "url": f"https://youtube.com/watch?v={item['id']}"
    } for item in res["items"]]
