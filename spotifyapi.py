import spotipy
from config import CLIENT_ID, CLIENT_SECRET, PLAY_LIST, USER, DIRECT_URI
from spotipy.oauth2 import SpotifyClientCredentials
import pandas
import numpy

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials( client_id=CLIENT_ID,
                                                                              client_secret=CLIENT_SECRET))

the_strokes_uri = 'https://open.spotify.com/artist/0epOFNiUfyON9EYx7Tpr6V'

results = spotify.artist_albums(the_strokes_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])