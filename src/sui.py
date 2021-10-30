import simpleaudio
from random import randint
from app.getch import getch

NUMBER_OF_FILES = 12
MEDIA_FOLDER_PATH = "./media/"

CODE_FILE_MAPPING = {
    1: 'file10.wav',
    2: 'file8.wav',
    3: 'file3.wav',
    5: 'file5.wav'
}
def play_test_sound():
    simpleaudio.WaveObject.from_wave_file('./media/file10.wav').play()

def get_filename(code):
    if code in CODE_FILE_MAPPING:
        return CODE_FILE_MAPPING[code]
    else:
        file_number = randint(1, NUMBER_OF_FILES)
        return 'file{}.wav'.format(file_number)

def main():
    play_test_sound()
    while True:
        ch = getch()
        if not ch.isnumeric():
            continue

        simpleaudio.stop_all()
        code = int(ch)
        filename = '{}{}'.format(MEDIA_FOLDER_PATH, get_filename(code))
        simpleaudio.WaveObject.from_wave_file(filename).play()

if __name__ == "__main__":
    main()

"""
play test sound on init
keep waiting for button input
on valid input
    kill any playing sound
    get code
    get a file based on code
    start playing sound asyncly

9 - random files
1 - shout siuu short file10.wav
2 - question siu file8.wav
3 - inshallah file3.wav
5 - special ofcourse - file5.wav

"""