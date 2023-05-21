from scrape import download_wav, search
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up the authentication flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='456d00237a8241de99b97d8b8f4f3254',
                                                           client_secret='34009c73ec7c4d1695abcbbd9b348501'))

search("New Jeans")