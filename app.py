from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))  # Nueva sintaxis

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text')
    response = client.chat.completions.create(  # Nueva sintaxis
        model="gpt-4",
        messages=[{"role": "user", "content": f"Resume esto en 5 puntos clave:\n{text}"}]
    )
    return jsonify({"summary": response.choices[0].message.content})

if __name__ == '__main__':
    app.run()
