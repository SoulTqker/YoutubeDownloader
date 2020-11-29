import pytube
import os
from time import sleep

username = os.getlogin()
video_list = []

print("Welcome aboard the trash Youtube-Downloader of the Wati-Dev")
sleep(1)
print('''
Wat you want?

(1) Download Vids Manually
(2) Downloads YouTube Playlist

''')


def res():
    resolution = quality
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    else:
        itag = 18
    return itag


def path():
    global chemin
    p = c
    if p.lower() in ['downloads', 'download']:
        chemin = f'C:/Users/{username}/Downloads'
    elif p.lower() in ['desktop']:
        chemin = f'C:/Users/{username}/Desktop'
    elif p.lower() in ['documents, document']:
        chemin = f'C:/Users/{username}/Documents'
    elif p.lower() in ['videos', 'video']:
        chemin = f'C:/Users/{username}/Videos'


    return chemin

def videos():
    print('Enter the url(s) (End by "STOP") :')
    while True:
        url = input("")
        if url.lower() == 'stop':
            break
        video_list.append(url)

    for x, video in enumerate(video_list):
        v = pytube.YouTube(video)
        stream = v.streams.get_by_itag(res())
        print(f'Downloading the video number {x}...')
        try:
            stream.download(output_path=path())
            print(f'Finished for the number {x}')
        except:
            print("sry it's not working for this video, trying for the next video...")
            pass
    return print("Done my brudda, your video(s) have been downloaded!")

def playlist():

    print("Enter the Playlist url :")
    url = input("")
    playlist = pytube.Playlist(url)
    for url in playlist:
        video = pytube.YouTube(url)
        stream = video.streams.get_by_itag(22)
        try:
            stream.download(output_path=path())
        except:
            print("sry it's not working for a video, trying for the next video...")
            pass
    return print("It's gud dude, your Playlist have been downloaded!")


choice = input("Bad choice: ")

if choice == "1" or choice == "2":
    quality = input("Choose your resolution (360p, 720p): ")
    c = input("Choose your downloading folder : Downloads, Desktop, Documents, Videos :")
    if choice == "1":
        videos()
    if choice == "2":
        playlist()
