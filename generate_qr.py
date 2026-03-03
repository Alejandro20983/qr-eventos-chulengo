import qrcode

url = "lively-zuccutto-4e6bf7.netlify.app/prueba.pdf"

qr = qrcode.QRCode(
    version = 1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_prueba.png")

print("QR code generated and saved as qr_prueba.png")