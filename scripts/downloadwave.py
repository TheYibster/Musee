from spFunctions import download_wav
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import wave
import os
import pandas as pd
import numpy as np

df = pd.read_csv('../csvData/cleanUrl.csv')
songs = df['url']
for i in range(len(songs)):
    download_wav(songs[i], os.path.join(os.getcwd(), "wavData" + f"{i}.wav"))



    

