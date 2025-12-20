# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_client import AIClient  # Import your AIClient

app = Flask(__name__)
CORS(app)

ai = AIClient()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    ai_response = ai.answer_question(user_message)
    return jsonify({'response': ai_response})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
