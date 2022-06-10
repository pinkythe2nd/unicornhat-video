from fileinput import filename
import pygame as pg
import pickle
import unicornhathd
import time
import threading
import argparse

def loadPickle(filename):
    picklefile = open(filename, "rb")
    array = pickle.load(picklefile)
    picklefile.close()
    return array

def play(data, duration):
    pg.mixer.Sound.play(pg.sndarray.make_sound(data))
    time.sleep(duration)

def renderLoop(filename):
    pg.mixer.init()
    unicornhathd.rotation(0)
    unicornhathd.brightness(1)
    u_width, u_height = unicornhathd.get_shape()
    array = loadPickle(filename)
    duration = array.pop(1)
    framesPerSec = len(array) / duration
    wait = (1000 / framesPerSec) / 1000
    frame = 0
    print(duration)
    x = threading.Thread(target=play, args=(array.pop(0), duration, ), daemon=True)
    x.start()
    try:
        for i in array:
            startTime = time.time()
            for y in range(u_height):
                for x in range(u_width):
                    #print(f"x: {x}, y: {y}\n r: {int((i[y][x]))*10}, g: {int(i[y][x])*10} b: {int(i[y][x])*10}")
                    unicornhathd.set_pixel(x, y, i[y][x][2], i[y][x][1], i[y][x][0])

            unicornhathd.show()
            print(f"Frame: {frame} rendered")
            frame += 1
            timeToSleep = wait - (time.time() - startTime)
            if timeToSleep > 0:
                time.sleep(timeToSleep)
    except KeyboardInterrupt:
        unicornhathd.off()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "reads in a pickled 2d array and displays them on the hat")
    parser.add_argument("-i", "--input", help = "Name of the file to be read in", required = True)
    args = parser.parse_args()
    renderLoop(args.input)

