#pip install PyQRCode or go to https://pypi.org/project/PyQRCode/#files
value = str(input("Enter the value of the QR-Code: "))

qr = pyqrcode.create(value)
qr.svg("qrcode.svg", scale = 8)

stop = str(input("QR-Code Created Successfully"))
