from pytube import YouTube

link = str(input("Enter the link: "))
url = link
video = YouTube(url)

print("Downloading :", video.title)
print("Thumbnail : ", video.thumbnail_url)

video = video.streams.get_highest_resolution()
video.download()

print("Installed Succesfully")