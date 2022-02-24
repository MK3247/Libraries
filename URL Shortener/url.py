import bitly_api

BITLY_ACCESS_TOKEN = '5f014fe33837a6484e83fde89d5a3f81fe536ec9'

access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

full_link = input('\n\n Enter URL: ')

short_url = access.shorten(full_link)

print('Short URL: ', short_url['url'])