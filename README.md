# Marathi Stopwords Library

A Python library for Marathi language text preprocessing.

This library provides useful tools for Marathi Natural Language Processing (NLP), including tokenization, stopword removal, stopword counting, custom stopword management, and a special power function that handles the edge case 0^0 = 0.

---

## Features

✅ Marathi stopword list

✅ Tokenization of Marathi text

✅ Remove stopwords from Marathi sentences

✅ Count stopwords in text

✅ Add custom stopwords

✅ Custom power function with:

```python
safe_pow(0, 0) == 0
```

---

## Project Structure

```text
marathi_stopwords/
│
├── __init__.py
├── stopwords.py
├── processor.py
└── math_utils.py

tests/
└── test_library.py

README.md
setup.py
demo.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/nupurmohite42-alt/marathi-stopwords-library.git
```

Move into the project directory:

```bash
cd marathi-stopwords-library
```

Install the package:

```bash
pip install .
```

---

## Usage

### Import Functions

```python
from marathi_stopwords import (
    tokenize,
    remove_stopwords,
    count_stopwords,
    add_stopword,
    get_stopwords,
    safe_pow
)
```

---

### Tokenization

```python
text = "मी आज शाळेत जात आहे"

print(tokenize(text))
```

Output:

```python
['मी', 'आज', 'शाळेत', 'जात', 'आहे']
```

---

### Remove Stopwords

```python
text = "मी आज शाळेत जात आहे"

print(remove_stopwords(text))
```

Output:

```python
शाळेत जात
```

---

### Count Stopwords

```python
text = "मी आज शाळेत जात आहे"

print(count_stopwords(text))
```

Output:

```python
3
```

---

### Add Custom Stopword

```python
add_stopword("शाळेत")
```

---

### Get Stopwords

```python
print(get_stopwords())
```

---

### Safe Power Function

```python
print(safe_pow(0, 0))
```

Output:

```python
0
```

Unlike Python's built-in behavior:

```python
0 ** 0
```

which returns:

```python
1
```

this library returns:

```python
0
```

to satisfy the assignment requirement.

---

## Running Tests

Run the test suite:

```bash
python tests/test_library.py
```

Expected Output:

```text
All Tests Passed Successfully!
```

---

## Demo

Run the demo program:

```bash
python demo.py
```

---

## Author

**Nupur Mohite**

Python Library Development Assignment Project

---

## License

This project is intended for educational and learning purposes.