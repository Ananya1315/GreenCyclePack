from flask import Flask, request, jsonify, render_template
from suggest_box import suggest_box

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    length = float(request.form['length'])
    width = float(request.form['width'])
    height = float(request.form['height'])

    suggestion = suggest_box(length, width, height)
    return render_template('result.html', suggestion=suggestion)

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
