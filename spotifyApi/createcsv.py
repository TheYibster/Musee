from spFunctions import download_wav, search
import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os
import librosa

# Set up the authentication flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='456d00237a8241de99b97d8b8f4f3254',
                                                           client_secret='34009c73ec7c4d1695abcbbd9b348501'))

wavPath = os.path.join(os.getcwd(), "wavData")

def wavToArr(wav_file_path):
    y,sr = librosa.load(wav_file_path)
    return list(y), int(sr)

def writeCSV(data):
    filename = 'data.csv'

    # Writing data to the CSV file
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    else:
        data.pop(0)
        csv_file = 'data.csv'

        # Append data to the CSV file
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)


def main():

    done = False

    while not done:
        query = input("Please Enter a Search Query: ")
        n = int(input("Number of times to search with this query(numeric): "))

        data = search(query, n)

        download = input("would you like to download the wav files now(y/n): ")
        if download == "y":
            for i in range(len(data)):
                if i == 0:
                    pass
                else:
                    download_wav(data[i][2], os.path.join(wavPath, str(i) + ".wav"))
            print("Files downloaded successfully.")
        else: 
            pass

        arr_status = input("would you like to convert wave to arrays now(y/n): ")
        if arr_status == "y":
            for i in range(len(data)):
                if i == 0:
                    data[0].append("arr")
                    data[0].append("sr")
                else:
                    arr, sr = wavToArr(os.path.join(wavPath, str(i) + ".wav"))
                    data[i].append(arr)
                    data[i].append(sr)
        else: 
            pass
        

        writeCSV(data)

        status = input("Do you want to add Another Query(y/n): ")
        if status == "y":
            for filename in os.listdir(wavPath):
                file_path = os.path.join(wavPath, filename)
                
                # Check if the path is a file
                if os.path.isfile(file_path):
                    # Delete the file
                    os.remove(file_path)
            pass
        else:
            done = True

    print("csv successfully downloaded to path.")

main()

