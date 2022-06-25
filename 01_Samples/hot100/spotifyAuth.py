import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENTID = "xxxxx"
CLIENTSECRET = "yyyy"


def get_auth() -> spotipy.client.Spotify:
    scope = "playlist-modify-private"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri="http://example.com",
        client_id=CLIENTID,
        client_secret=CLIENTSECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
    )
    return sp

print(type(get_auth()))
