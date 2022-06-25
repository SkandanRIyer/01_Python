from bs4 import BeautifulSoup
import requests
import spotifyAuth as Auth
import spotipy

sp = Auth.get_auth()
user_id = sp.current_user()["id"]
list_date = input("Which Year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
base_url = "https://www.billboard.com/charts/hot-100/"

url = base_url + list_date
print(url)
year = list_date.split("-")[0]

response = requests.get(url)
top_100_list = response.text

soup = BeautifulSoup(top_100_list, "html.parser")
song_titles = [song.getText().strip() for song in soup.select(selector="li h3", class_="title-of-a-story")]
song_titles = song_titles[:100:1]
print(song_titles)
song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify")

print(len(song_uris))

# result = sp.user_playlists(user=user_id, limit=10,offset=0)
# print(result)


result = sp.user_playlist_create(user=user_id, name=f"{list_date} Billboard 100", public=False, description=f"Top 100 Songs on {list_date}")
print(result["id"])
result = sp.playlist_add_tracks(playlist_id=result["id"], items=song_uris)
print(result)
