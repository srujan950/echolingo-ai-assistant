import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Google AI API
try:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in .env file")
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Error configuring Google AI: {e}")

# Initialize the Flask app
app = Flask(__name__)

# This is the main page
@app.route('/')
def index():
    return render_template('index.html')

# This is the endpoint our JavaScript will call
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        question = data.get('question')
        language = data.get('language')

        if not question or not language:
            return jsonify({'error': 'Missing question or language'}), 400

        # Create the model and generate content
        model = genai.GenerativeModel('gemini-1.5-flash-latest') # Using a reliable model
        prompt = f"Answer the following question in {language}: {question}"
        response = model.generate_content(prompt)

        return jsonify({'answer': response.text})

    except Exception as e:
        print(f"Error during analysis: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)