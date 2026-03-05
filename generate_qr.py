import qrcode

url = "lively-zuccutto-4e6bf7.netlify.app/Flyer_Chulengo.jpg"

qr = qrcode.QRCode(
    version = 1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("Flyer_Chulengo.jpg")

print("QR code generated and saved as Flyer_Chulengo.jpg")