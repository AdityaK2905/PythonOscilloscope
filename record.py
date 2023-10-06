import soundcard as sc
import soundfile as sf
from matplotlib import pyplot as plt
import wave
import io

import pygame
OUTPUT_FILE_NAME = "out.wav"    # file name.
SAMPLE_RATE = 48000              # [Hz]. sampling rate.
RECORD_SEC = 3                  # [sec]. duration recording audio.

pygame.init()
my_font = pygame.font.SysFont('Times New Roman', 30)


win = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Visualizer")
my_font = pygame.font.SysFont('Times New Roman', 30)


text_surface = my_font.render('Some Text', False, (0, 0, 0))
win.blit(text_surface, (0,0))

dataM = None

with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
    # record audio with loopback from default speaker.
    data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)
    dataM = data
    #print(data.size)
    #print(data)
    # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
    sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)

print(dataM)
for x in range(1, 1000):
    #print(dataM[x][1])
    plt.plot(dataM[x][1])


# with io.BytesIO() as wav_file:
#     wav_writer = wave.open(wav_file, "wb")
#     try:
#         wav_writer.setframerate(SAMPLE_RATE)
#         wav_writer.setsampwidth(3)
#         wav_writer.setnchannels(2)
#         wav_writer.writeframes(data)
#         wav_data = wav_file.getvalue()
#     finally:
#         wav_writer.close()


sf.write(file="remade.wav", data=dataM, samplerate=SAMPLE_RATE)
plt.plot(dataM)
plt.show()