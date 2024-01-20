from spFunctions import download_wav
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import wave
import os
import pandas as pd
import numpy as np

df = pd.read_csv('./csvData/cleanUrl.csv')
for i in df.loc[:,'url']:
    download_wav(i)


print(df.head())


    

