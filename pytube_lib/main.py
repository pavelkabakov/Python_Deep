from pytube import YouTube

# ссылка на загружаемое видео
link = "https://youtu.be/lSIwOUv_Qn4?si=QLyyMLfHLk-AGhie"
yt = YouTube(link)
print(yt.streams)
yt = YouTube(link).streams.get_highest_resolution()

yt.download()
# yt.streams.first().download()
print("Видео успешно загружено")