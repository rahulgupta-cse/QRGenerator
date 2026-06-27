#Program to generate QR Code for text message, links,Youtube video link 
import qrcode
from PIL import Image

url = input("Enter the URL or message You want to Display:\n")
filename = input("Enter the file name to save QR (without .png): ")

qr = qrcode.QRCode(version =1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,) 
qr.add_data(url)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white") #QR image style
img.save(filename + ".png")
print("QR Code generated and saved as", filename + ".png")
