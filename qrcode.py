import qrcode

# 要链接的特定页面URL
page_url = "https://www.axfff.com/archive/JGA2023"

# 创建QR码对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 向QR码添加数据（URL）
qr.add_data(page_url)
qr.make(fit=True)

# 创建QR码图像
qr_img = qr.make_image(fill_color="black", back_color="white")

# 保存QR码图像到文件
qr_img.save("special_page_qr.png")