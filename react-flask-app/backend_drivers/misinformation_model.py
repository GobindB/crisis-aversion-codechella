import pandas as pd
from spellchecker import SpellChecker

# take tweet and pass it to the model


def calculate_validity_score(tweet, reconstructed_model, keywords):
    # initialize list of lists TODO: fix location
    processed_text = process_text(tweet.text)
    data = [[tweet.id, keywords.join("%20"), "California", processed_text]]

    prediction_df = pd.DataFrame(
        data, columns=['id', 'keyword', 'location', 'text'])
    prediction = reconstructed_model.predict(prediction_df)
    return prediction

# data processing


def process_text(tweet_text):
    tweet_text = remove_URL(tweet_text)
    tweet_text = remove_html(tweet_text)
    tweet_text = remove_emoji(tweet_text)
    tweet_text = remove_punct(tweet_text)
    tweet_text = correct_spellings(tweet_text)
    pass


def remove_URL(text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'', text)


def remove_html(text):
    html = re.compile(r'<.*?>')
    return html.sub(r'', text)

# Reference : https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b


def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def remove_punct(text):
    table = str.maketrans('', '', string.punctuation)
    return text.translate(table)


spell = SpellChecker()


def correct_spellings(text):
    corrected_text = []
    misspelled_words = spell.unknown(text.split())
    for word in text.split():
        if word in misspelled_words:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    return " ".join(corrected_text)
