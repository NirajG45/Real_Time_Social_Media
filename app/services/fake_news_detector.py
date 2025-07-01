from transformers import pipeline
classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fakenews")

def check_fake(text):
    result = classifier(text)
    return result[0]['label'], result[0]['score']
