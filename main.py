
import pyaudio
import wave
import sys

sound  = True
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 6
WAVE_OUTPUT_FILENAME = "output.wav"




with wave.open('output.wav', 'wb') as wf:
    p = pyaudio.PyAudio()

    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    stream = p.open(format = FORMAT,
                channels = 0,
                rate = RATE,
                input = True,
                input_device_index = 32,
                )


    for i in range(p.get_device_count()):
        print(p.get_device_info_by_index(i))
    
    # for i in range(p.get_device_count()):
    
    #     dev = p.get_device_info_by_index(i)
    #     if (dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0):
    #         dev_index = dev['index']
    #         print('dev_index', dev_index)
    #     
    print('Recording...')
    
    
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        wf.writeframes(stream.read(CHUNK))
    print('Done')

    stream.close()
    p.terminate()