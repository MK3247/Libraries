import pafy 

v = pafy.new('https://www.youtube.com/watch?v=J9f_uZuDcOM&ab_channel=PPPTV')

#methods - getbest(), getbestaudio(), getbestvideo
# Stream methods can be used to access the following Stream attributes
# Stream attributes - url, url_https, bitrate, rawbitrate, extension, quality, resolution, mediatype, dimension, notes

best_video = v.getbestvideo() #getting best video stream
best_audio = v.getbestaudio() #getting best audio stream

print('Video Streams: ',v.streams)
print('Audio Streams: ', v.audiostreams)
print('Best Audio Stream: ', best_audio)
print('Video Streams*: ', v.videostreams)
print('Best Video Stream: ', best_video)
print('Ogg Streams: ', v.oggstreams) #Empty for some videos
print('M4A Streams: ', v.m4astreams)
print('All Streams: ', v.allstreams)
print('\n')
print('Stream Attributes')
print('\n')
print('Best audio streams: ', best_audio)
print('\n')
print('Title: ', best_audio.title)
print('Quality: ', best_audio.quality)
print('Bitrate: ', best_audio.bitrate)
print('Raw bitrate: ', best_audio.rawbitrate)
print('Dimension: ', best_audio.dimensions)
print('Extension: ', best_audio.extension)
print('Resolution: ', best_audio.resolution)
print('Media type: ', best_audio.mediatype)
print('Url: ', best_audio.url)
print('Url_https: ', best_audio.url_https)
print('\n')
print('Best Video: ', best_video)
print('Title: ', best_video.title)
print('Quality: ', best_video.quality)
print('Dimensions: ', best_video.dimensions)
print('Resolution: ', best_video.resolution)
print('Media type: ', best_video.mediatype)
print('Extensions: ', best_video.extension)
print('URl: ', best_video.url)
print('URL HTTPS: ', best_video.url_https)
print('Notes: ', best_video.notes)