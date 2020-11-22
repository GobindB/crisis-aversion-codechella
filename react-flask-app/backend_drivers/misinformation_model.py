from tensorflow import keras
import string
import re

from numpy.matrixlib.defmatrix import matrix
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from pandas.core.frame import DataFrame
# from spellchecker import SpellChecker
import pandas as pd
import numpy as np
from tqdm import tqdm
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))


reconstructed_model = keras.models.load_model("my_model")
# take tweet and pass it to the model


def calculate_validity_score(tweet, reconstructed_model, keywords):
    # initialize list of lists TODO:
    # fix location add .
    processed_text = process_text(tweet.'text')

    data = [[tweet.id, keywords.join("%20"), "California", processed_text]]

    prediction_df = pd.DataFrame(
        data, columns=['id', 'keyword', 'location', 'text'])

    corpus = create_corpus(prediction_df)
    prediction_df = instantiate_matrix(prediction_df, corpus)
    prediction = reconstructed_model.predict(prediction_df)
    return prediction

# data processing


def process_text(tweet_text):
    tweet_text = remove_URL(tweet_text)
    tweet_text = remove_html(tweet_text)
    tweet_text = remove_emoji(tweet_text)
    tweet_text = remove_punct(tweet_text)
    # tweet_text = correct_spellings(tweet_text)
    return tweet_text


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


# spell = SpellChecker()


def correct_spellings(text):
    corrected_text = []
    misspelled_words = spell.unknown(text.split())
    for word in text.split():
        if word in misspelled_words:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    return " ".join(corrected_text)


def create_corpus(df):
    corpus = []
    for tweet in tqdm(df['text']):
        words = [word.lower() for word in word_tokenize(
            tweet) if((word.isalpha() == 1) & (word not in stop))]
        corpus.append(words)
    return corpus


def instantiate_matrix(df, corpus):
    embedding_dict = {}
    with open('glove.6B.100d.txt', 'r') as f:
        for line in f:
            values = line.split()
            word = values[0]
            vectors = np.asarray(values[1:], 'float32')
            embedding_dict[word] = vectors
    f.close()

    MAX_LEN = 50
    tokenizer_obj = Tokenizer()
    tokenizer_obj.fit_on_texts(corpus)
    sequences = tokenizer_obj.texts_to_sequences(corpus)

    print(corpus)
    print(sequences)

    word_index = tokenizer_obj.word_index
    num_words = len(word_index)+1
    embedding_matrix = np.zeros((num_words, 100))

    for word, i in tqdm(word_index.items()):
        if i > num_words:
            continue

        emb_vec = embedding_dict.get(word)
        if emb_vec is not None:
            embedding_matrix[i] = emb_vec

    tweet_pad = pad_sequences(
        sequences, maxlen=MAX_LEN, truncating='post', padding='post')

    print(tweet_pad)
    return tweet_pad
