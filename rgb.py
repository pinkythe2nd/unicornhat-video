import numpy as np
from PIL import Image
import sys

np.set_printoptions(threshold=sys.maxsize)

cols = 16
rows = 16
scale = 1

def getAverageRGB(image):
    return list(image.getdata())

def covertImageToRGB(fileName):
    global rows

    image = Image.fromarray(fileName)
 
    W, H = image.size[0], image.size[1]
 
    w = W/cols
    h = H/rows
    #rows = int(H/h)
 
    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)
 
    # ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
 
        # correct last tile
        if j == rows-1:
            y2 = H
 
        # append an empty string
        aimg.append([])

        for i in range(cols):
            aimg[j].append([])
            # crop image to tile
            x1 = int(i*w)
            x2 = int((i+1)*w)
 
            # correct last tile
            if i == cols-1:
                x2 = W

            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))
            
            aimg[j][i] += getAverageRGB(img)[i]
            # get average rgb
            # append ascii char to string
            #hi = int(getAverageRGB(img))
            #hitwo = int((hi * 9) / 255)
            #aimg[j] += str(hitwo)

            #print(aimg[-1])
     
    # return txt image
    return aimg

def RGB(imgFile):
    aimg = covertImageToRGB(imgFile)
    array = []
    
    for row in aimg:
        array.append(row)

    return array
    # cleanup