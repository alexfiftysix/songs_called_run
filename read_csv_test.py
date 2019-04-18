import pandas as pd
import json
from pandas.io.json import json_normalize
import statistics
import collections

file = open('only_good_data.csv', 'r')
dataframe = pd.read_csv(file)

print(dataframe)