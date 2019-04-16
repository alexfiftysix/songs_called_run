import requests

song = 'run'
artist = 'street pieces'

url = "https://api.spotify.com/v1/search?q=" + song + "%20" + artist + "&type=track&limit=1"
headers = {'Authorization': '962aaa2d14f64a1c963d9b08dfadaffc:588f405f6d9d44b1ae5f8ca3a75b9b50'}

response = requests.post(url)

print(response)
print(response.content)
