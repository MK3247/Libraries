from fileinput import filename
import pafy 

v = pafy.new('https://www.youtube.com/watch?v=HWZnmZRxOvI&list=RDHWZnmZRxOvI&start_radio=1&ab_channel=ZojakWorldWideOfficial')

best_audio = v.getbestaudio()
size = best_audio.get_filesize()

print('File Name: ', best_audio.title)
print('Size: ', size)

filename = best_audio.download()

best_video = v.getbestvideo()
size = best_video.get_filesize()

print('File Name: ', best_video.title)
print('Size: ', size)

filename = best_video.download()