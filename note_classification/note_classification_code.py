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
import copy

trumpet_path =  '../sound_samples/trumpet'
cello_path =  '../sound_samples/cello'
sax_path = '../sound_samples/saxophone'

CONCERT_PITCH = 440
ALL_NOTES = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
NUM_HPS = 8

def find_closest_note(pitch):
  i = int( np.round( np.log2( pitch/CONCERT_PITCH )*12 ) )
  closestNote = ALL_NOTES[i%12] + str(4 + np.sign(i) * int( (9+abs(i))/12 ) )
  closestPitch = CONCERT_PITCH*2**(i/12)
  return closestNote, closestPitch

def get_peak(rate, data, useHPS):
    
    samp_period = 1. / rate
    num_data_points = len(data)

    frequencies = np.linspace(0,1,num_data_points) * rate

    fft_out = fft(data)
    abs_fft = np.abs(fft_out)

    peak_location = None
    if useHPS:
      hpsSpec = copy.deepcopy(abs_fft)
      for i in range(NUM_HPS):
        tmpHpsSpec = np.multiply(hpsSpec[:int(np.ceil(len(abs_fft)/(i+1)))], abs_fft[::(i+1)])
        if not any(tmpHpsSpec):
          break
        hpsSpec = tmpHpsSpec

      maxInd = np.argmax(hpsSpec)
      peak_location = frequencies[maxInd]

    else:
      maxInd = np.argmax(abs_fft)
      peak_location = frequencies[maxInd]



    return peak_location

def read_files(path, useHPS):
    files = os.listdir(path)
    errors = 0
    for file in files:
        if file.endswith(".wav"):
            rate, data = wavfile.read(path + '/' + file)
            peak = get_peak(rate, data, useHPS)
            note, pitch  = find_closest_note(peak)
            real_note = file.split("_")[1]
            if real_note[1] == 's':
              real_note = real_note[0] + '#' + real_note[2]
            if real_note != note:
              print(pitch)
              print(note)
              print(real_note)
              errors+=1
    print("Error")
    print(errors/len(files))
    print(len(files))

print("trumpet")
read_files(trumpet_path, True)
print("\n\n")
print("cello")
read_files(cello_path, True)


