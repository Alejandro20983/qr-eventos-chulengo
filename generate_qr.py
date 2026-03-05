import qrcode

url = "https://lively-zuccutto-4e6bf7.netlify.app/chulengo_final.jpg"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("Flyer_Chulengo_QR_final.jpg")

print("QR code generated and saved as Flyer_Chulengo_QR_final.jpg")