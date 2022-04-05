import pyqrcode

value = str(input("Enter the value of the QR-Code: "))

qr = pyqrcode.create(value)

qr.svg("qrcode.svg", scale = 8)

stop = str(input("QR-Code Created Successfully"))