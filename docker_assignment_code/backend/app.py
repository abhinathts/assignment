from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

@app.route('/process', methods=['POST'])
def process_form():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify({"message": f"Hello {name}, welcome!"})

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)
