from utils.QR import generate_qr

box_info = {
    "box_id": "GREENBOX01",
    "dimensions": [34, 20.5, 12.5],
    "material": "Recycled Rigid Cardboard",
    "co2_saved": 0.5,
    "cost_saved": 2.8
}

generate_qr(box_info, "greenbox01_qr")
