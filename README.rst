=================
FCMC Data Scraper
=================

Alfie Zhang
May 2022

Setup
=====

See requirements.txt

First run the following:

1. source env/bin/activate
2. pip install beautifulsoup4
3. pip install lxml

How to use
==========

Start venv from root of scraper:
* $ source env/bin/activate

Scraper commands:
-----------------
To run:

* $ python3 scraper1.py

Currently, input path is set inside of scraper.py file.
Output file path is set to User/Downloads by default. This can be changed in the generator.py file.

When done, deactivate venv:

* $ deactivate

