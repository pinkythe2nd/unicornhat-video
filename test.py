import pygame as pg
import pickle
import time
import threading
import unicornhathd
import argparse

def load(filename):
    pickleFile = open(f"{filename}", "rb")
    pickledArray = pickle.load(pickleFile)
    return pickledArray

def play(data, duration):
    pg.mixer.Sound.play(pg.sndarray.make_sound(data))
    time.sleep(duration + 1)

def main(filename):
    pg.mixer.init()
    array = load(filename)
    duration = array.pop(1)
    x = threading.Thread(target=play, args=(array.pop(0), duration, ), daemon=True)
    frames = len(array)
    time_for_each_frame = duration / frames
    x.start()
    for frame in array:
        start = time.time()
        for x in range(16):
            for y in range(16):
                unicornhathd.set_pixel(x, y, frame[x][y][0], x[x][y][1], x[x][y][2])
        unicornhathd.show()
        end = time.time()
        time_taken = end - start
        if time_taken < time_for_each_frame:
            time.sleep(time_for_each_frame - time_taken)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= "input a filename of a video and returns a serialized 2D array of 16 * 16 numbers of each frame of the video")
    parser.add_argument("-i", "--input", help="url to download", required=True)
    args = parser.parse_args()

    main(args.input)
