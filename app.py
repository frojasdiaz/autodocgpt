from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_KEY")

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text')
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Resume esto en 5 puntos clave:\n{text}"}]
    )
    return jsonify({"summary": response.choices[0].message.content})

if __name__ == '__main__':
    app.run()
