import os
from flask import Flask, request, jsonify, render_template
from suggest_box import suggest_box
from utils.QR import generate_qr
from user_data import save_user_box_info


app = Flask(__name__)

# Absolute path to static/QRCodes
QR_DIR = os.path.join(os.path.dirname(__file__), 'static', 'QRCodes')
os.makedirs(QR_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    try:
        length = float(request.form['length'])
        width = float(request.form['width'])
        height = float(request.form['height'])

        if length <= 0 or width <= 0 or height <= 0:
            return "❌ Invalid dimensions. All values must be greater than 0.", 400

        suggestion = suggest_box(length, width, height)
        user_id = request.form.get('user_id', 'demo_user')  # default fallback
        save_user_box_info(user_id, suggestion)


        # ✅ QR Data
        qr_data = f"""Box ID: {suggestion['box_id']}
Dimensions: {suggestion['dimensions']}
Material: {suggestion['material']}
CO₂ Saved: {suggestion['co2_saved']} kg
Cost Saved: ₹{suggestion['cost_saved']}"""

        qr_filename = f"{suggestion['box_id']}"
        qr_path = os.path.join(QR_DIR, qr_filename)

        generate_qr(qr_data, qr_path)

        # ✅ HTML needs relative URL
        qr_image_url = f"/static/QRCodes/{qr_filename}"

        return render_template('result.html', suggestion=suggestion, qr_image=qr_image_url)

    except Exception as e:
        return f"❌ Error: {str(e)}", 500

@app.route('/suggest_box', methods=['POST'])
def api_suggest_box():
    data = request.get_json()
    length = data['length']
    width = data['width']
    height = data['height']
    result = suggest_box(length, width, height)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
