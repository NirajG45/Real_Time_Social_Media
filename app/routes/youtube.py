from flask import Blueprint, jsonify
from app.services.fetch_youtube import get_youtube_trending
from app.services.fake_news_detector import check_fake
from app.services.location_extractor import extract_location

youtube_bp = Blueprint("youtube", __name__, url_prefix="/api/youtube")

@youtube_bp.route("/")
def fetch_youtube():
    posts = get_youtube_trending()
    enriched = []
    for post in posts:
        label, score = check_fake(post['title'])
        location = extract_location(post['title'])
        enriched.append({
            "title": post['title'],
            "url": post['url'],
            "label": label,
            "confidence": round(score * 100, 1),
            "location": location
        })
    return jsonify(enriched)
