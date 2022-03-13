import qrcode 

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://www.youtube.com/watch?v=DLRfecGZhts&ab_channel=DWDocumentary')

qr.make(fit=True)

image = qr.make_image(fill_color = 'black', back_color = 'white')

image.save('img.png')