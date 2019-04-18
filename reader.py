import json
from collections import Counter
import pandas

data = open('track_data.json', 'r')
read = data.read()
song_info = json.loads(read)

print(song_info["href"])

album_types = set()
album_count = 0
single_count = 0
compilation_count = 0

release_dates = []

for i in range(len(song_info["items"])):
    print(song_info['items'][i]['track'])
    print('artist: {}'.format(song_info['items'][i]['track']['artists'][0]['name']))
    print('duration: {}'.format(song_info['items'][i]['track']['duration_ms']))
    print('popularity: {}'.format(song_info['items'][i]['track']['popularity']))

    release_date = song_info['items'][i]['track']['album']['release_date']
    print('release date: {}'.format(release_date))
    release_year = release_date[:4]
    release_dates.append(release_year)

    album_type = song_info['items'][i]['track']['album']['album_type']
    print('album type: {}'.format(album_type))
    album_types.add(album_type)

    if album_type == 'single':
        single_count += 1
    elif album_type == 'album':
        album_count += 1
    elif album_type == 'compilation':
        compilation_count += 1

    print('album name: {}'.format(song_info['items'][i]['track']['album']['name']))
    print('id: {}'.format(song_info['items'][i]['track']['id']))
    print('-' * 50)

print('-' * 50)
print('single count: {}'.format(single_count))
print('album count: {}'.format(album_count))
print('compilation count: {}'.format(compilation_count))

print('-' * 50)
release_dates = Counter(release_dates)
print('release dates: ')
print(sorted(release_dates.items()))
print('-' * 50)
ids = ''
count = 0

for i in range(len(song_info["items"])):
    ids += song_info['items'][i]['track']['id']
    ids += ','
    count += 1

print(ids[:-1])

""" 
Use audio features
"""
