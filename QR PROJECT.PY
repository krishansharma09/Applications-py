import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://www.learnvern.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("webpage.png")
# img = qr.make("https://www.learnvern.com/")
# img.save("krish.png")
# print("code successfully ganrated")