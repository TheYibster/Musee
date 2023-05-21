import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import wave

def download_wav(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
            print("File downloaded successfully.")
            # Check if the downloaded file is a valid WAV file
            try:
                wave.open(filename)
            except wave.Error:
                print("The downloaded file is not a valid WAV file.")
    else:
        print("Failed to download the file.")

# Set up the authentication flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='456d00237a8241de99b97d8b8f4f3254',
                                                           client_secret='34009c73ec7c4d1695abcbbd9b348501'))

def search(query):
    results = sp.search(q=query, type='track', market="NA")
    results = (results["tracks"]["items"][0]['preview_url'], results["tracks"]["items"][0]['name'])
    print(results)
    return results



