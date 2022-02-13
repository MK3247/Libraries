import pafy 

v = pafy.new("https://www.youtube.com/watch?v=J9f_uZuDcOM&ab_channel=PPPTV")

print('Title: ', v.title)
print('Category: ', v.category)
# print('Description: ', v.description)
print('Author: ', v.author)
# print('Published: ', v.published)
print('Thumbnail: ', v.thumb)
print('Thumb Nail (HD): ', v.bigthumbhd)
print('Ratings: ', v.rating)
print('Duration in HH:MM:SS: ', v.duration)
print('Length in seconds: ', v.length)
print('Likes: ', v.likes)
print('Dislikes: ', v.dislikes)
print('Video ID: ', v.videoid)
print('Username: ',v.username)
print('View count: ', v.viewcount)