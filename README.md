# Data Science: Semester 4

Descriptive statistics written from scratch in plain Python, for a 4th-semester data science course.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## About

`operation.py` computes basic statistics on a small hard-coded list of heights. It uses hand-written helpers instead of library functions like `statistics` or NumPy.

## What It Covers

- **Helper functions**
  - `findLen`: counts list elements without `len()`
  - `sort`: a simple nested-loop exchange sort
  - `shuffle`: a hand-written random shuffle (Fisher-Yates style)
  - `custom_root`: an integer square-root search, plus `root`, a wrapper around `math.sqrt`
- **Statistics**
  - Mean
  - Median (handles both odd- and even-length lists)
  - Mode, using a frequency map (prints a message when every value is distinct)
  - Population variance and standard deviation

## Running

Needs Python 3 and no extra packages.

```bash
python operation.py
```

The script prints the shuffled list, then the mean, median, mode, standard deviation and variance.

## Author

**Aryan Bhandari**: [GitHub](https://github.com/aryanbha123)
