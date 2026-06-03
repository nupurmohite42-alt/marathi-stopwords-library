from .stopwords import MARATHI_STOPWORDS
def get_stopwords():
    return MARATHI_STOPWORDS

def add_stopword(word):
    MARATHI_STOPWORDS.add(word)

def tokenize(text):
    return text.split()

def remove_stopwords(text):

    words = text.split()

    filtered = []

    for word in words:

        if word not in MARATHI_STOPWORDS:

            filtered.append(word)

    return " ".join(filtered)

def count_stopwords(text):

    words = text.split()

    count = 0

    for word in words:

        if word in MARATHI_STOPWORDS:

            count += 1

    return count

def safe_pow(base, exp):

    if base == 0 and exp == 0:
        return 0

    return base ** exp


