from marathi_stopwords import (
    tokenize,
    remove_stopwords,
    safe_pow,
    count_stopwords
)

text = "मी आज शाळेत जात आहे"

print("Original:", text)
print("Tokens:", tokenize(text))
print("After Stopword Removal:", remove_stopwords(text))
print("Stopword Count:", count_stopwords(text))
print("0^0 =", safe_pow(0,0))
