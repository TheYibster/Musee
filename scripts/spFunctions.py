import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import wave
import os

# Set up the authentication flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='456d00237a8241de99b97d8b8f4f3254',
                                                           client_secret='34009c73ec7c4d1695abcbbd9b348501'))


def download_wav(url, file_path = os.path.join(os.getcwd(), "wavData")):
    response = requests.get(url)

    if response.status_code == 200:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'wb') as file:
            file.write(response.content)
    else:
        print("Failed to download the file.")

# Usage example
# wav_url = 'https://example.com/example.wav'
# output_file_path = '/path/to/output/output.wav'
# download_wav(wav_url, output_file_path)

def search(query,limit=5):
    # Parameters: 
    #     query: the search query [str]
    #     limits: how manys tracks to query from the spotify api [int] 
    # Return:
    #      List of Tuples [("Name", "Popularity", "Track Url"),...]
    results = sp.search(q=query, type="track", market="NA", limit=limit)
    lst = [["name", "popularity", "url"]]
    for i in range(limit):
        lst.append([results["tracks"]["items"][i]['name'], 
        results["tracks"]["items"][i]['popularity'], 
        results["tracks"]["items"][i]['preview_url']])

    return lst

