# 📊 RealTrend Analyzer

A **real-time social media analyzer** built with **Python and Flask** that fetches trending content from **YouTube**, **Instagram**, and **LinkedIn**, detects **fake news**, extracts **location information**, and displays it on a live dashboard.

---

## 🎯 Objective

Track what’s trending on social media and answer:
- ✅ Is the content **Real or Fake**?
- 📍 **Where** did the incident happen?
- 📅 **When** did the event occur?
- 📺 Show trending **videos, posts, and news** in a structured UI.

---

## ⚙️ Tech Stack

| Layer         | Technology Used                           |
|--------------|--------------------------------------------|
| Frontend     | HTML, JavaScript (Fetch API)               |
| Backend      | Python, Flask                              |
| APIs         | YouTube Data API, HuggingFace Transformers, spaCy |
| NLP Models   | - Fake News Detection: `bert-tiny-finetuned-fakenews`  
              - Location Extraction: `en_core_web_sm`       |
| Environment  | `.env` file for API keys                   |

---

## 🏗️ Architecture Diagram

```plaintext
        ┌──────────────┐
        │  Frontend    │  ← HTML + JS (Fetch API)
        └────┬─────────┘
             │
             ▼
     ┌────────────────┐
     │ Flask Backend  │
     └────────────────┘
     ┌────────────┬────────────┬─────────────┐
     ▼            ▼            ▼             ▼
[YouTube]   [Instagram]   [LinkedIn]   (others in future)
     │            │            │
     ▼            ▼            ▼
[Fake News Detector] ← HuggingFace Transformers
[Location Extractor] ← spaCy NLP
     │
     ▼
 Enriched JSON Response → Frontend → Rendered Dashboard
