import simpleaudio
from numpy.random import randint

from app.getch import getch

NUMBER_OF_FILES = 2

def play_test_sound():
    simpleaudio.WaveObject.from_wave_file('./media/file1.wav').play()

play_test_sound()

print('press 0 to exit')

while True:
    ch = getch()
    print(ch, flush=True)

    if ch == '0':
        exit()
    if not ch.isnumeric():
        continue
    code = int(ch)

    simpleaudio.stop_all()
    file_number = randint(1, NUMBER_OF_FILES+1)
    file_name = './media/file{}.wav'.format(file_number)
    simpleaudio.WaveObject.from_wave_file(file_name).play()



"""
play test sound on init
display codes?
keep waiting for button input
on input
    kill any playing sound
    pick a random file
    start playing sound asyncly
"""