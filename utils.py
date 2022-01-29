import qrcode
from flask import current_app
import os

def generate_qrcode(qrcode_url, file_name):

    """Function to generate qr code
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qrcode_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    image_name = os.path.join(current_app.config["QR_FOLDER"], file_name+".png")
    img.save(image_name)

    return image_name