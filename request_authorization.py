import requests

url = 'https://accounts.spotify.com/authorize'

client_id = '962aaa2d14f64a1c963d9b08dfadaffc'
client_secret = '588f405f6d9d44b1ae5f8ca3a75b9b50'

data = {
    'client_id': client_id,
    'response_type': 'token',
    'redirect_uri': 'https://www.google.com/',
}

response = requests.get(url, data=data)

print(response)

print(response.content)
