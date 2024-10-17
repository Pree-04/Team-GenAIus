from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os
from dotenv import load_dotenv
import google.generativeai as genai
from markdown import markdown  # Import markdown library for rendering Markdown

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for requests from the frontend

# Load environment variables for the API key
load_dotenv (dotenv_path= "C:/Users/preet/Downloads/GenAIus/config/.env")

# Configure Gemini AI API key
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    logging.error("API key is not set in environment variables.")
    exit(1)

# Create a model instance
model = genai.GenerativeModel("gemini-1.5-flash")  # Use your required model

# Function to generate a response from the generative model
def generate_response(user_question, cleaned_text):
    try:
        prompt = f"""
        - Using the knowledge base, answer the following question: '{user_question}'. Here is the information: {cleaned_text}.
        - If you cannot find anything in the context document, generate a relevant answer yourself.
        - The text should be formal, friendly, and professional.
        - Understand the context. 
        - Some of the text data contains json data about transactions, reviews, and product pricing. If any questions are asked related to json data, please answer them.
        - The final output should be raw text that may include Markdown formatting.
        - You are a domain speccific chatbot and you only answer knowledge management, knowledge transfer related and educational queries or questions and doubts.
        """
        
        response = model.generate_content([prompt])
        
        return response.text if hasattr(response, 'text') else "No response content found."
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return "An error occurred while generating the response."

# API endpoint to handle user queries
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json  # Get data from the POST request
    user_question = data.get('message')

    if not user_question:
        return jsonify({"error": "No message provided"}), 400
    
    # Load cleaned text from the file
    file_path = r"C:\Users\preet\Downloads\GenAIus\Data Pre processing\all_cleaned_data.txt"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            cleaned_text = file.read()
    except FileNotFoundError:
        return jsonify({"error": "Knowledge base not found."}), 500

    # Generate response from the model
    bot_response = generate_response(user_question, cleaned_text)

    # Convert the bot's response to HTML using Markdown
    bot_response_html = markdown(bot_response)

    # Send the bot's response back to the frontend
    return jsonify({"reply": bot_response_html})

if __name__ == '__main__':
    app.run(debug=True)
