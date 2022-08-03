#pip install pytube, or go to https://github.com/pytube/pytube.git
from pytube import YouTube

video = YouTube(str(input("Enter the link of the video: ")))

print("Downloading : ", video.title)
print("Thumbnail : ", video.thumbnail_url)

video = video.streams.get_highest_resolution()
video.download()

print("Downloaded Succesfully")
