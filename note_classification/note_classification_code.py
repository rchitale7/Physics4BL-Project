# read in sound files
# perform fourier transform
# create matrix/table with accuracy of note classification

import os
from scipy.fftpack import fft
from scipy import signal
from scipy.io import wavfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

trumpet_path =  '../sound_samples/trumpet'
cello_path =  '../sound_samples/cello'
sax_path = '../sound_samples/saxophone'


def read_files(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".wav"):
            rate, data = wavfile.read(path + '/' + file)
            print(rate)
read_files(trumpet_path)

