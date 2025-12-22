'''
Frontend_app.py this is the main Flask application file that sets up the server and defines the API endpoints for chat and quiz generation.
'''


from flask import Flask, request, jsonify
from flask_cors import CORS

from services.ai_client import AIClient
from services.quizz_service import QuizzService
from services.user_creation import create_profile, get_profile, users_collection

app = Flask(__name__)

CORS(app, origins=[
    "http://localhost:3000",  
    "https://*.netlify.app"   
])


ai = AIClient()


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        ai_response = ai.answer_question(user_message)
        return jsonify({"response": ai_response})
    except Exception as e:
        print(f"Error creating chat: {e}")
        return jsonify({"error": "Failed to process message"}), 500


@app.route('/quiz/generate', methods=['POST'])
def generate_quiz():
    try:
        data = request.get_json() or {}
        topic = data.get("topic", "natural disasters")
        num_questions = data.get("questions", 5)

        quiz_service = QuizzService(topic=topic)
        quiz_data = quiz_service.generate_quizz(topic=topic, questions=num_questions)
        
        result = {"questions": quiz_data}    
        return jsonify(result)


    except Exception as e:
        print(f"Error creating quiz: {e}")
        return jsonify({"error": str(e)}), 500

# route to create a new user profile
@app.route('/user/create', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        country = data.get('country')
        city = data.get('city')
        age = data.get('age')
        
        user_id = create_profile(name, email, country, city, age)
        return jsonify({"user_id": str(user_id)}), 201
    
    except Exception as e:
        print(f"Error creating user: {e}")
        return jsonify({"error": str(e)}), 500

# route to login user by email
@app.route('/user/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        email = data.get('email')
        
        # Procura user por email
        from services.user_creation import users_collection
        user = users_collection.find_one({"email": email})
        
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        user["_id"] = str(user["_id"])
        return jsonify(user), 200
        
    except Exception as e:
        print(f"Error logging in: {e}")
        return jsonify({"error": str(e)}), 500

#route to get user profile by user_id
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = get_profile(user_id)
        return jsonify(user), 200
    except Exception as e:
        print(f"Error getting user: {e}")
        return jsonify({"error": str(e)}), 404    


if __name__ == "__main__":
    app.run(port=5000, debug=True)
