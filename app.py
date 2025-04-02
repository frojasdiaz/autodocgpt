from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
HF_API_KEY = os.getenv("HF_API_KEY")  # Nueva variable de entorno

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text')
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"  # Modelo gratuito
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    return jsonify({"summary": response.json()[0]['summary_text']})

if __name__ == '__main__':
    app.run()
