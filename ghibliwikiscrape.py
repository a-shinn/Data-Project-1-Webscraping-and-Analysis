import pandas as pd
import numpy as np
import bs4 as bs
import requests

tables = pd.read_html('https://en.wikipedia.org/wiki/Studio_Ghibli')
print(tables[0])
print()
print(tables[1])
