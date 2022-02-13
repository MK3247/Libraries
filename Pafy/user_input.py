import pafy

url = input("Enter video url: ")

video = pafy.new(url)

best_audio = video.getbestaudio()

audio_size = best_audio.get_filesize()

print('Title: ', video.title)
print('Author: ', video.author)
print('Size: ', audio_size)
print('Downloading...')

filename = best_audio.download()