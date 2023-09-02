import requests
from bs4 import BeautifulSoup
import datetime as dt
import warnings
warnings.filterwarnings('ignore')
try:
    date=input("which year do you want to go?Type a date in the format YYYY/MM/DD?")
    url=f"https://www.billboard.com/charts/hot-100/{date}"
    response=requests.get(url)
    data=response.text
    soup=BeautifulSoup(data,"html.parser")
    song_name=soup.findAll(name="h3", class_="a-no-trucate")
    list_of_song_name=[]
    for x in song_name:
        list_of_song_name.append(x.getText().strip())
    a=' '.join([str(elem+"\n") for elem in list_of_song_name])
    print(a)
except TypeError:
    print('Invalid Date')

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=cc447ee682634db1a6f8ac50923b8e66,
        client_secret=dfc07497dd5a4521b675c5732305ca42,
        show_dialog=True,
        cache_path="token.txt",
        username="054cj4yit9t6h7m7e1ulhhh0s",
    )
)
user_id = sp.current_user()["id"]