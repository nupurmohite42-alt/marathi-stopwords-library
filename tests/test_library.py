from marathi_stopwords import (
    tokenize,
    remove_stopwords,
    safe_pow,
    count_stopwords,
    get_stopwords
)

# Test 1
assert tokenize(
    "मी आज शाळेत जात आहे"
) == ['मी', 'आज', 'शाळेत', 'जात', 'आहे']

# Test 2
assert safe_pow(0,0) == 0

# Test 3
assert remove_stopwords(
    "मी आज शाळेत जात आहे"
) == "शाळेत जात"

# Test 4 (Extra)
assert count_stopwords(
    "मी आज शाळेत जात आहे"
) == 3

print("All Tests Passed Successfully!")

