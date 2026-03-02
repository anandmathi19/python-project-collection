import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import spotipy

SPOTIFY_CLIENT_ID = "your id"
SPOTIFY_CLIENT_SECRET = "Your secret code"

travelling_year = input("Which year do you want to travel to? "
                        "Type the date in this format yyyy-MM-DD: ")
year = travelling_year.split("-")[0]

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

URL = f"https://www.billboard.com/charts/hot-100/{travelling_year}"

response = requests.get(URL, headers= header)
html_website = response.text

soup = BeautifulSoup(html_website, "html.parser")
all_songs = soup.select("li ul li h3")

songs = [song.get_text().strip() for song in all_songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="https://example.com",
    scope="playlist-modify-private"
))

spotify_uri = []

for song in songs:
    try:
        query = f"track: {song} year: {year}"
        result = sp.search(q=query, type="track", limit=1)
        tracks = result["tracks"]["items"][0]
        uri = tracks["uri"]
        spotify_uri.append(uri)

    except IndexError:
        print(f"song not found: {song}")

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id,
                                       name=f"{travelling_year} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=spotify_uri)
print("Playlist created and trcaks added")


