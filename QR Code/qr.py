import qrcode 

img = qrcode.make('https://pypi.org/project/pyzbar/')

img.save('pyzar.png')