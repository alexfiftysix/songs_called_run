import pandas as pd
import json
from pandas.io.json import json_normalize
import statistics
import collections

data = open('audio_features.json', 'r')
read = data.read()
_json = json.loads(read)

audio_features_df = json_normalize(_json['audio_features'])  # has id

data = open('track_data.json', 'r')
read = data.read()
_json = json.loads(read)

track_and_album_data_df = json_normalize(_json["items"])  # has track.id
# track_data_df = track_and_album_data_df['track']


merged = pd.merge(left=audio_features_df, right=track_and_album_data_df, left_on='id', right_on='track.id')
merged['track.album.release_date'] = pd.to_datetime(merged['track.album.release_date'])
print(merged.sort_values(by=['track.album.release_date']))

print(merged['track.album.release_date'])



