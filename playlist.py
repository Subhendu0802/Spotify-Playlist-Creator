import datetime as dt
import warnings
warnings.filterwarnings('ignore')
import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to go? Type a date in the format YYYY-MM-DD: \n")
url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url)
status=response.raise_for_status()  # Raise an exception for HTTP errors
data = response.text
soup = BeautifulSoup(data, "html.parser")
song_name = soup.select("li ul li h3")
list_of_song_name = [x.getText().strip() for x in song_name]#list comprehension
print(list_of_song_name)
print(len(list_of_song_name))