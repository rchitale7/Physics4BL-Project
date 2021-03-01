# read in sound files
# perform fourier transform
# create matrix/table with accuracy of note classification

import os
from scipy.fftpack import fft
from scipy import signal
from scipy.signal import find_peaks
from scipy.io import wavfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

trumpet_path =  '../sound_samples/trumpet'
cello_path =  '../sound_samples/cello'
sax_path = '../sound_samples/saxophone'

CONCERT_PITCH = 440
ALL_NOTES = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
def find_closest_note(pitch):
  i = int( np.round( np.log2( pitch/CONCERT_PITCH )*12 ) )
  closestNote = ALL_NOTES[i%12] + str(4 + np.sign(i) * int( (9+abs(i))/12 ) )
  closestPitch = CONCERT_PITCH*2**(i/12)
  return closestNote, closestPitch

def get_peak(rate, data):
    samp_period = 1. / rate
    num_data_points = len(data)
    fft_out = fft(data)
    abs_fft = np.abs(fft_out)

    # Create an array that goes from 0 to the 44100 Hz
    frequencies = np.linspace(0,1,num_data_points) * rate
    plt.plot(frequencies,np.abs(fft_out))
    plt.xlim([100, 1000])

    peaks, _ = find_peaks(abs_fft, height= 2700000, distance = 30* num_data_points/rate)
    peaks = peaks[peaks > 50 * num_data_points/rate] #Makes the minimum frequency for a peak be 200 Hz

    # Find the maximum value of the Fourier transform
    max_value = np.max(abs_fft)

    # Find the index where the max location is
    max_location = np.where(abs_fft == max_value)[0][0]

    # Now we find the frequency where this happens
    peak_location = frequencies[max_location]
    return peak_location

def read_files(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".wav"):
            rate, data = wavfile.read(path + '/' + file)
            peak = get_peak(rate, data)
            note, pitch  = find_closest_note(peak)
            real_note = file.split("_")[1]
            print("Predicted: ")
            print(note)
            print("Real")
            print(real_note)
            print("\n")

read_files(trumpet_path)

