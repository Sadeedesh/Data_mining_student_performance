def preprocessing(text):
    return text.lower().strip()

def vectorizer(text):
    return [text]

def get_prediction(vectorized_text):
    return 'positive'
