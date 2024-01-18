import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os
import librosa
import random

from spFunctions import download_wav, search

# Set up the authentication flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='456d00237a8241de99b97d8b8f4f3254',
                                                           client_secret='34009c73ec7c4d1695abcbbd9b348501'))

wavPath = os.path.join(os.getcwd(), "wavData")


with open('./Musee/spotifyApi/word.txt') as f:
    words = f.read().splitlines()

randomwords = []
for i in random.sample(range(10000), 10000):
    randomwords.append(words[i])

randomData = []
for word in randomwords:
    randomData.append(pd.DataFrame(search(word, 1)[1:], columns=("name", "popularity", "url")))

print(randomData)

my_df = pd.concat(randomData)
my_df.to_csv("url.csv", index=False)
