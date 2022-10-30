from pytube import YouTube
link = "https://youtu.be/BGp8fkpQu2M"
youtube_1 = YouTube(link)
print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all() #All streams
videos = youtube_1.streams.filter(only_audio=True)  #only audio
vid = list(enumerate(videos)) # labelling the index to the items of the list
for i in vid:
    print(i)
str = int(input("Enter the streams")) #taking input from the user to download in the desired stream
videos[str].download() # download the video
print('Download succesfully')


# FOR COMPLETE PLAYLIST

from pytube import Playlist
py = Playlist('link of the video')

print(f'Downloading {py.title}')

for video in py.videos():
    video.streams.first().download()



