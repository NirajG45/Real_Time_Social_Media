import spacy
nlp = spacy.load("en_core_web_sm")

def extract_location(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            return ent.text
    return "Unknown"
