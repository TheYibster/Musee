import pandas as pd
import numpy as np

data = pd.read_csv("/Users/yiboliang/Projects/weTheArtist/weTheArtist/spotifyApi/data.csv")

print(data.head())

print(data["url"])