# Data Project 1 - NGE

Repository for my data project to analyze the characters and script of Neon Genesis Evangelion. My initial inspiration was drawn from a data visualization for The Office (link: https://public.tableau.com/app/profile/kasia.gasiewska.holc/viz/DwightSchrutesSurveillanceSystem/SurveillanceSystem).

The goal of this project was to practice my skills through the entire data pipeline from beginning to end, that is, gathering, cleaning, storage, feature engineering, analysis, and visualization.
For this project I wanted to use Python as I've been self-studying and wanted to solidify what I've learned. Overall I'm very happy with this project and how it turned out, as I learned a lot and became much more comfortable coding with Python and its syntax, as well as working with new packages by researching their documentation. I initially started the project using PyCharm as my IDE but later moved to Jupyter Notebook as I found the ability to run smaller blocks of code useful for analysis and to save time and server load on the website that I pulled scripts from (source: https://www.animanga.com/scripts/anime_scripts_english.html).

The notebook files that I used for webscraping and data analysis are in the main folder, final visualizations are located in the visualizations_final folder, and datasets created and files used are in the src folder.

Notes for further analysis:
- the translation that I used is accurate enough for general numeric analysis, but not ideal for finer analysis. The numbers are only mostly accurate as the translations were done as a fan project and there are numerous typos for character names and their actual dialogue. If a better dataset were available the analysis would be more accurate, but overall the quality is good enough to work with.
- Due to the typos, statistics such as the number of unique words per character couldn’t be accurate with all the misspellings and so I avoided adding this feature in. A spellchecking program using NLP could be used to correct character names and misspellings.
- A sentiment analysis could also be done for each character as in the visualization for The Office, but I considered adding in NLP/machine learning models to be a bit out of scope of this project, as my main goal and focus was to work through stages of the data pipeline and grow my familiarity with Python.

Thank you for reading!

--------------------

Packages used
--------------------

Pandas

Numpy

BeautifulSoup4

Re

Requests

Time

Matplotlib

Plotly

PIL

WordCloud

Stop_words

Scipy

--------------------

Skills:
--------------------

Python

Jupyter Notebook

Pandas

Webscraping

JSON

Regex

Data Gathering

Data Cleaning

Feature Engineering

Data Analysis

Data Visualization
