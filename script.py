import cv2, pickle, os, argparse
from audio import audioit
from rgb import RGB
from youtubeDownloader import downloadVHS

def extractImagesRGB(fileIn, fileOut):
    count = 0
    threeDArray = []#intialize variables

    threeDArray.append(audioit(fileIn)) #add audio

    #---compress mp4 to make it quicker---#
    vidcap = cv2.VideoCapture(fileIn)
    fps = vidcap.get(cv2.CAP_PROP_FPS) 
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    threeDArray.append(frame_count / fps)
    success, image = vidcap.read() #start going through frame by frame
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count*60)) 
        success, image = vidcap.read()
        image = cv2.flip(image, 1)
        if (success):
            array = RGB(image)
            threeDArray.append(array)

        count += 1
        print(f"frame: {count}")
    print(f"rendered: {count}, outputfile: {fileOut}")
    
    with open(fileOut, 'wb') as fo:
        pickle.dump(threeDArray, fo, 2)
    
    #os.remove(fileIn)y

if __name__ == "__main__":
    outputFile = "outputFile"
    rgb = False
    parser = argparse.ArgumentParser(description = "input a filename of a video and returns a serialized 2D array of 16 * 16 numbers of each frame of the video")
    parser.add_argument("-i", "--input", help = "url to download", required=True)
    parser.add_argument("-o", "--output", help = "name of the output file", required=False)
    args = parser.parse_args()

    if args.output:
        outputFile = args.output

    downloadVHS(args.input)
    extractImagesRGB("vhs.mp4", outputFile)