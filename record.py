import sys
import wave
import pyaudio


def record(fname):

    # the numbers
    RATE = 44100
    CHUNK = 4096
    FORMAT = pyaudio.paInt16

    # begin recording
    print('****************')
    _ = input('Press enter to start the recording')

    # save to a wave file
    with wave.open(fname, 'wb') as wf:

        # prepare the file
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(RATE)

        print('Press ctrl-C to end recording')

        # create the audio object
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT,
                            channels=1,
                            rate=RATE,
                            input=True,
                            output=True)

        # record until interrupted
        while True:

            try:
                wf.writeframes(stream.read(CHUNK))
            except KeyboardInterrupt:
                break

    # end of fun!
    print('\nDone recording')
    print('****************')

    return None

if __name__ == '__main__':
   
    try:
        name = sys.argv[1]
    except IndexError:
        name = 'test.wav'

    record(name)
    


