import qrcode

# QR kodunu oluşturmak istediğiniz linki buraya girin
url = "https://www.example.com"

# QR kodu oluşturma
qr = qrcode.QRCode(
    version=1,  # QR kodun boyutunu ayarlayabilirsiniz
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# QR kodunu resim olarak oluşturma
img = qr.make_image(fill='black', back_color='white')

# QR kodunu kaydetme
img.save("qr_code.png")
