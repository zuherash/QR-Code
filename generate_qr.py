import qrcode

url = "https://castera-plus.vercel.app/"
img = qrcode.make(url)
img.save("castera_plus_qr.png")
print("QR code saved to castera_plus_qr.png")
