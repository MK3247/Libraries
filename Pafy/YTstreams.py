import pafy 

v = pafy.new('https://www.youtube.com/watch?v=J9f_uZuDcOM&ab_channel=PPPTV')

#methods - getbest(), getbestaudio(), getbestvideo

best_video = v.getbestvideo()
best_audio = v.getbestaudio()

print('Video Streams: ',v.streams)
print('Audio Streams: ', v.audiostreams)
print('Best Audio Stream: ', best_audio)
print('Video Streams*: ', v.videostreams)
print('Best Video Stream: ', best_video)
print('Ogg Streams: ', v.oggstreams) #Empty for some videos
print('M4A Streams: ', v.m4astreams)
print('All Streams: ', v.allstreams)