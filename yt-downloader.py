from pytube import YouTube

url = str(input("Enter the link: "))
video = YouTube(url)

print("Downloading :", video.title)
print("Thumbnail : ", video.thumbnail_url)

video = video.streams.get_highest_resolution()
video.download()

print("Downloaded Succesfully")

