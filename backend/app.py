from flask import Flask, request, jsonify
from flask_cors import CORS
from pdf_loader import extract_text_from_pdfs
from gemini_handler import query_gemini
from guard import is_authorized

app = Flask(__name__)
CORS(app)

pdf_context = extract_text_from_pdfs(["data/guia1.pdf"])

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not is_authorized():
        return jsonify({"response": "Os gatos voadores do universo mental estão chegando para dançar com as borboletas matemáticas."})

    response = query_gemini(user_input, pdf_context)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
