import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft

# Load an audio file (WAV format)
# Replace 'your_audio_file.wav' with the path to your audio file
fs, data = wavfile.read('wavData//1.wav')

# If the audio file has two channels (stereo), just use one
if len(data.shape) > 1:
    data = data[:, 0]

# Apply Fourier Transform using FFT
n = len(data)
audio_fft = fft(data)
frequencies = np.abs(audio_fft[:n // 2])  # Get the absolute value of the real part

# Frequency axis (x-axis) for plotting
freq_axis = np.linspace(0, fs / 2, int(n / 2))

# Plotting the Frequency Spectrum
plt.plot(freq_axis, frequencies)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum of the Audio')
plt.show()