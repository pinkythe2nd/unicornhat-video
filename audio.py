import pydub as pd
import pygame as pg
import pickle
import os

def mp3it(filename):
    audio = pd.AudioSegment.from_file(filename, "mp4")
    audio.export("export.wav", format="wav", bitrate="64k")

def pickleIt():
    pgSoundObject = pg.mixer.Sound("export.wav")
    return pg.sndarray.array(pgSoundObject)

def load(filename):
    pickleFile = open(f"{filename}.f", "rb")
    pickledArray = pickle.load(pickleFile)
    return pg.sndarray.make_sound(pickledArray)

def audioit(filename):
    pg.init()
    mp3it(filename)
    array = pickleIt()
    os.remove("export.wav")
    print("Audio Sorted! : Returning!")
    return array
