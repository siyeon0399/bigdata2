import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm?dayTime=2022041715'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
song_list = soup.select('tr[data-song-no]')

for song in song_list:
    rank = song.select_one('.rank').text
    title = song.select_one('.ellipsis.rank01').a.text
    artist = song.select_one('.ellipsis.rank02').a.text
    print(rank, '.', title, '-', artist)
