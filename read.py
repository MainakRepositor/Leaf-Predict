# Read data from csv

import numpy as np
import pandas as pd

df = pd.read_csv('leaf_data.csv')
df.head(10)

print(df.info())

