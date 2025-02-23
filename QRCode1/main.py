import qrcode
import qrcode.constants
import qrcode.image.svg

# ---

# img = qrcode.make("ChuChuMan loves ChuChuWoman!")
# img.save(f"qr_code\\myqrcode.png")

# ---

# qr = qrcode.QRCode(version=1, 
#                    error_correction=qrcode.constants.ERROR_CORRECT_L,
#                    box_size=50, 
#                    border=2)

# qr.add_data("https://www.neuralnine.com/books")
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")
# img.save(f"qr_code\\advanced.png")

# ---

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World!", image_factory=factory)
svg_img.save(f"qr_code\\myqr.svg")
