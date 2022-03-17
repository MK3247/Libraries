import pyqrcode 

import png 

from pyqrcode import QRCode

s = 'https://www.youtube.com/playlist?list=PLeo1K3hjS3us_ELKYSj_Fth2tIEkdKXvV'

url = pyqrcode.create(s) #generates qrcode 

# url.svg('code.svg', scale = 8) #save in svg format

url.png('code.png', scale = 8)

