import qrcode
import os

def generate_qr(data, box_id):
    # Get absolute path to backend/static/QRCodes
    base_dir = os.path.dirname(__file__)  # utils/
    static_qr_dir = os.path.join(base_dir, '..', 'static', 'QRCodes')
    os.makedirs(static_qr_dir, exist_ok=True)

    # Full path to save the QR image
    filename = f"{box_id}"
    filepath = os.path.abspath(os.path.join(static_qr_dir, filename))

    # Generate and save QR
    img = qrcode.make(data)
    img.save(filepath)

    # Return the relative URL path Flask can serve
    return f"/static/QRCodes/{filename}"
