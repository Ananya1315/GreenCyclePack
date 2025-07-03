from flask import Flask, request, jsonify, render_template
from suggest_box import suggest_box

app = Flask(__name__)

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
        return render_template('result.html', suggestion=suggestion)

    except Exception as e:
        return f"❌ Error: {str(e)}", 500


# Your existing /suggest_box POST API stays here
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
