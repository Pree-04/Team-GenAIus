import os
import logging
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from model import get_clean_text, generate_embeddings, generate_response
from markdown import markdown  # Import markdown library for rendering Markdown

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Enable CORS for specific route

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables for API key
load_dotenv()

# Configure the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    logging.error("API key is not set in the environment variables.")
    exit(1)

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load and preprocess the text data
file_path = os.path.join(BASE_DIR, "AllCleanData.txt")  # Adjust file name if necessary
raw_text = get_clean_text(file_path)
if raw_text is not None:
    logging.info("Text data loaded successfully.")
    embeddings = generate_embeddings(raw_text)
    if embeddings is not None:
        logging.info("Embeddings generated successfully.")
    else:
        logging.error("Failed to generate embeddings.")
else:
    logging.error("Failed to read cleaned text.")

# API endpoint to handle chat requests
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message')

        if user_message:
            # Generate a response based on user input and loaded text
            bot_response = generate_response(user_message, raw_text)
            # Convert the bot's response to HTML using Markdown
            bot_response_html = markdown(bot_response)

            # Send the bot's response back to the frontend
            return jsonify({"reply": bot_response_html})
        else:
            return jsonify({"reply": "No message received"}), 400
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"reply": "Error processing your request"}), 500

# Run the app
if __name__ == '__main__':
    app.run(port=5000)
