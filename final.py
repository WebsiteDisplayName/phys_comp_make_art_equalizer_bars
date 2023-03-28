import digitalio
from adafruit_debouncer import Button
import random
from audiopwmio import PWMAudioOut as AudioOut
from audiomp3 import MP3Decoder
import board
import time
import busio
import sdcardio
import storage
import mount_sd
import os
from audiocore import WaveFile


audio = AudioOut(board.GP16)
path = "/sd/make_art/"

song_list = os.listdir(path)
print(song_list)


button_input = digitalio.DigitalInOut(board.GP9)  # Wired to GP12
button_input.switch_to_input(digitalio.Pull.UP)
button = Button(button_input)  # NOTE: False for external buttons


def play_sound(filename):
    with open(path + filename, "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            button.update()
            if button.released:
                break


prev = -1
while True:
    val = random.randint(0, len(song_list)-1)
    if val != prev:
        prev = val
        play_sound(song_list[val])
