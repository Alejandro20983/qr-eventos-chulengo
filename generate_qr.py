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
img.save("Flyer_Chulengo2.jpg")

print("QR code generated and saved as Flyer_Chulengo2.jpg")