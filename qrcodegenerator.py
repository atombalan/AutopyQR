#importing necessary libraries
import pyqrcode 
from pyqrcode import QRCode 

#Taking input from the user
s = input('Enter the string to be QR Coded\n')

#generating the QR
url = pyqrcode.create(s)

#Saving the file
url.svg("qrcode.svg", scale = 8)

#atombalan



