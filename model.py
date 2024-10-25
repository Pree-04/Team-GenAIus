import os
import logging
import json
from dotenv import load_dotenv
import google.generativeai as genai

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
    exit(1)  # Exit the program if API key is not available

# Create a model instance
model = genai.GenerativeModel("gemini-1.5-flash")  # Adjust the model name as needed

# Function to list available models
def list_available_models():
    try:
        models = genai.list_models()
        model_names = [model.name for model in models]  # Extracting model names
        logging.info("Available models: " + ", ".join(model_names))
    except Exception as e:
        logging.error(f"Error listing models: {e}")

# Function to read cleaned text from file with error handling
def get_clean_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        return None

# Function to generate embeddings for the cleaned data and save them to a JSON file
def generate_embeddings(content, output_file="embeddings.json", chunk_size=2000):
    model_name = "models/text-embedding-004"
    embeddings = []
    
    # Split the content into chunks
    for i in range(0, len(content), chunk_size):
        chunk = content[i:i + chunk_size]
        try:
            chunk_embeddings = genai.embed_content(content=chunk, model=model_name)
            embeddings.append(chunk_embeddings)
        except Exception as e:
            logging.error(f"Error embedding content: {e}")
            continue

    # Save the embeddings to a file
    if embeddings:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(embeddings, f, ensure_ascii=False, indent=4)
            logging.info(f"Embeddings saved successfully to {output_file}")
        except Exception as e:
            logging.error(f"Error saving embeddings to file: {e}")
            return None

    return embeddings

# Function to generate a response from the generative model using RAG
def generate_response(user_question, cleaned_text):
    try:
        prompt = (f"Using the knowledge base, answer the following question: '{user_question}'. "
                  f"Here is the information: {cleaned_text}. "
                  "If you cannot find relevant information, generate it. "
                  "Respond professionally as 'your onboarding buddy' with a friendly tone.")
        
        response = model.generate_content([prompt])  # Use the model instance
        return response.text if hasattr(response, 'text') else "No response content found."
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return "An error occurred while generating the response."

def main():
    # Get the directory of the current script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # File paths using absolute paths
    file_path = os.path.join(BASE_DIR, "AllCleanData.txt")  # Adjust if necessary
    output_file = os.path.join(BASE_DIR, "embeddings.json")

    logging.info("Processing cleaned data...")
    raw_text = get_clean_text(file_path)
    if raw_text is not None:
        logging.info("Text data loaded successfully.")
        
        logging.info("Listing available models...")
        list_available_models()

        # Generate embeddings and save to file
        embeddings = generate_embeddings(raw_text, output_file=output_file)
        if embeddings is not None:
            logging.info("Embeddings generated and saved successfully.")
        else:
            logging.error("Failed to generate embeddings.")
            return
    else:
        logging.info("Failed to read cleaned text.")
        return

    # Take user queries in the console
    while True:
        user_question = input("\nAsk a question from the cleaned data (or type 'exit' to quit): ")
        if user_question.lower() == 'exit':
            break
        answer = generate_response(user_question, raw_text)
        print("Reply from Gemini: ", answer)

if __name__ == "__main__":
    main()
