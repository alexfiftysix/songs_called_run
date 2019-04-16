import json

data = open('data.json', 'r')
read = data.read()
j = json.loads(read)

print(j["href"])

for i in range(len(j["items"])):
    print(j['items'][i]['track'])
    print('artist: {}'.format(j['items'][i]['track']['artists'][0]['name']))
    print('duration: {}'.format(j['items'][i]['track']['duration_ms']))
    print('popularity: {}'.format(j['items'][i]['track']['popularity']))
    print('release date: {}'.format(j['items'][i]['track']['album']['release_date']))
    print('album type: {}'.format(j['items'][i]['track']['album']['album_type']))
    print('album name: {}'.format(j['items'][i]['track']['album']['name']))
    print('id: {}'.format(j['items'][i]['track']['id']))
    print('-' * 50)

ids = ''
count = 0

for i in range(len(j["items"])):
    ids += j['items'][i]['track']['id']
    ids += ','
    count += 1

print(ids[:-1])

""" 
Use audio features
"""
