import youtube_dl
import os

ytdl_format_options = {
    "format": "worst",
    "outtmpl": "input.mp4",
    "restrictfilenames": True,
    "nocheckcertificate": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
}

def downloadVHS(input):
    with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
        ydl.download([input])

    os.system("ffmpeg -i input.mp4 -vf scale=720x576,setdar=4/3 vhs.mp4")
    os.remove("input.mp4")
