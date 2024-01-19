from pytube import YouTube

# ссылка на загружаемое видео
link = "https://www.youtube.com/watch?v=J0Aq44Pze-w"
yt = YouTube(link)
print(yt.streams)
yt = YouTube(link).streams.get_highest_resolution()

yt.download()
# yt.streams.first().download()
print("Видео успешно загружено")