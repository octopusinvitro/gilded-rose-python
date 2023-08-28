# README

[Gilded Rose from Emily Bache](https://github.com/emilybache/GildedRose-Refactoring-Kata).

Uses the `approvaltests` library to create a Golden Master that can be used for refactoring. The commits show a step by step refactoring.

To install dependencies:

```bash
pip install --upgrade pip && pip install -r requirements.txt
```

To run the tests:

```bash
coverage run -m unittest discover -v
```

You can generate an HTML coverage report with:

```bash
coverage html
```
