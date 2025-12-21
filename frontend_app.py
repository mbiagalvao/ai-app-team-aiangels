'''
Frontend_app.py this is the main Flask application file that sets up the server and defines the API endpoints for chat and quiz generation.
'''


from flask import Flask, request, jsonify
from flask_cors import CORS

from services.ai_client import AIClient
from services.quizz_service import QuizzService

app = Flask(__name__)
CORS(app)

ai = AIClient()


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    ai_response = ai.answer_question(user_message)
    return jsonify({"response": ai_response})


@app.route('/quiz/generate', methods=['POST'])
def generate_quiz():
    try:
        data = request.get_json() or {}
        topic = data.get("topic", "natural disasters")
        num_questions = data.get("questions", 5)

        quiz_service = QuizzService(topic=topic)
        quiz_data = quiz_service.generate_quizz(topic=topic, questions=num_questions)

        print("QUIZ DATA:", quiz_data)
        print("TYPE:", type(quiz_data))
        
        result = {"questions": quiz_data}
        print("SENDING:", result)  # <-- Adiciona isto
        
        return jsonify(result)

    except Exception as e:
        print(f"Erro ao gerar quiz: {e}")
        import traceback
        traceback.print_exc()  # <-- Adiciona isto para ver o erro completo
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
