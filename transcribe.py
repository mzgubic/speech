import os
import wave
import json
import pyaudio
import record


def transcribe():

    # record the sound in a temporary file
    fname = 'tmp.wav'
    record.record(fname)

    # transcribe it
    os.system("gcloud ml speech recognize {} --language-code='en-US' > result.json".format(fname))

    # print to screen
    with open('result.json') as f:
        data = json.load(f)

    print(data['results'][0]['alternatives'][0]['transcript'])

if __name__ == '__main__':
   
    transcribe()


