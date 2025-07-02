import json

with open('data_box.json', 'r') as f:
    boxes = json.load(f)

def suggest_box(product_length, product_width, product_height):
    suitable_boxes = []

    for box in boxes:
        box_length, box_width, box_height = box["dimensions"]

        if (box_length >= product_length and
            box_width >= product_width and
            box_height >= product_height):
            
            box_volume = box_length * box_width * box_height
            suitable_boxes.append((box_volume, box))

    if not suitable_boxes:
        default_box = {
            "box_id": "GREENBOX_DEFAULT",
            "dimensions": [40, 30, 15],
            "material": "Recycled Cardboard",
            "co2_saved": 0.2,
            "cost_saved": 1.5
        }
        return {
            "note": "No exact fit found. Using default eco-box.",
            **default_box
        }

    best_box = min(suitable_boxes, key=lambda x: x[0])[1]
    return {
        "box_id": best_box["box_id"],
        "dimensions": best_box["dimensions"],
        "material": best_box["material"],
        "co2_saved": best_box["co2_saved"],
        "cost_saved": best_box["cost_saved"]
    }

#optional 
if __name__ == "__main__":
    l = float(input("Enter product length (cm): "))
    w = float(input("Enter product width (cm): "))
    h = float(input("Enter product height (cm): "))

    result = suggest_box(l, w, h)
    print("Suggested Eco-Box:", result)
