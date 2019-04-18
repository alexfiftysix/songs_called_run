import pandas as pd
import json
from pandas.io.json import json_normalize
import statistics
import collections

data = open('audio_features.json', 'r')
read = data.read()
_json = json.loads(read)

df = json_normalize(_json['audio_features'])

# pd.options.display.max_columns = 150
# pd.options.display.max_rows = 100
# pd.options.display.column_space = 200
# pd.options.display.latex.longtable = True

write_to = open('audio_features_table.csv', 'w')
write_to.write(df.to_csv())

print(df)
acousticness = df['acousticness']
instrumentalness = df['instrumentalness']
speechiness = df['speechiness']
tempo = df['tempo']
valence = df['valence']
duration_ms = df['duration_ms']
time_signature = df['time_signature']
loudness = df['loudness']


# print(list(acousticness))
# for a in acousticnesses:
#     print(a)

def print_stats_data(dataset):
    count = len(dataset)
    in_order = sorted(dataset)
    low = in_order[0]
    high = in_order[-1]
    median = statistics.median(dataset)
    mean = statistics.mean(dataset)

    print('count: {}\n\nlow: {}\nmean: {}\nmedian: {}\nhigh: {}'.format(count, low, mean, median, high))


print_stats_data(speechiness)
