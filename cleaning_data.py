import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('final_data.csv')
df.dropna(subset=['Gross_worldwide'], inplace=True)
df.reset_index(drop=True, inplace=True)

def parse_currency(before_parsed):
    if '$' in before_parsed:
        after_parsed = int(before_parsed.strip('$').replace(',', ""))
    else:
        after_parsed = int(int(before_parsed.strip('€').replace(',', "")) * 1.14)
    return after_parsed

