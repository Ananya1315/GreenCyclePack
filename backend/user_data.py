import json
import os
from datetime import datetime

# JSON path relative to this script (can be tweaked)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'user_data.json')

def save_user_box_info(user_id, box_info):
    # Load existing entries
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = []

    # Create new entry
    entry = {
        "user_id": user_id,
        "box_id": box_info["box_id"],
        "dimensions": box_info["dimensions"],
        "material": box_info["material"],
        "co2_saved": box_info["co2_saved"],
        "cost_saved": box_info["cost_saved"],
        "timestamp": datetime.now().isoformat()
    }

    data.append(entry)

    # Write updated data
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
