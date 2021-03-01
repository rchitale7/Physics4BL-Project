## Instructions for running note classification code:

1. Create a directory called sound_samples. (Path: Physics4BL-Project/sound_samples)
2. Download and unzip each instrument zip file
3. Run the following command on each instrument directory to move samples that don't match the string called "filter" to another directory:

`find . -maxdepth 1 -type f -not -name "*filter*" -exec mv {} /path/to/dir \;`

Alternatively, you can remove these unwanted files:

`find . -maxdepth 1 -type f -not -name "*filter*" -exec rm -rf {} \;`

4. Move each instrument directory to the sound_samples folder
5. note_classification/note_classification_code.py will now read .wav files from sound_samples directory. (e.g. to read a trumpet sound file, we would read from the path: Physics4BL-Project/sound_samples/trumpet/{name of trumpet file}.wav)
6. To run the classification, do: 

` cd note_classification`

`python note_classification_code.py`

## Instructions for running guitar_tuner/guitar_tuner.py

1. `pip install sounddevice` 

    or 

    `pip3 install sounddevice`
2. `cd guitar_tuner`
3. `python tuner.py`