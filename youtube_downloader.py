from pytube import YouTube
link = "https://youtu.be/BGp8fkpQu2M"
youtube_1 = YouTube(link)
print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
str = int(input("Enter the streams"))
videos[str].download()
print('Download succesfully')

