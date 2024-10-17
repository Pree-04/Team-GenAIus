import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables for API key
load_dotenv()

# Configure the Gemini API key
api_key = os.getenv("GOOGLE_API_KEY")
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

# Function to generate embeddings for the cleaned data
def generate_embeddings(content, chunk_size=2000):  # Set a chunk size smaller than the limit
    model_name = "models/text-embedding-004"  # Use the available text embedding model
    embeddings = []
    
    # Split the content into chunks
    for i in range(0, len(content), chunk_size):
        chunk = content[i:i + chunk_size]
        try:
            chunk_embeddings = genai.embed_content(content=chunk, model=model_name)
            embeddings.append(chunk_embeddings)
        except Exception as e:
            logging.error(f"Error embedding content: {e}")
            return None

    return embeddings  # Return all embeddings as a list

# Function to generate a response from the generative model using RAG
def generate_response(user_question, cleaned_text):
    try:
        # Format the prompt to guide the model for RAG
        prompt = f"""Using the knowledge base, answer the following question: '{user_question}'. Here is the information: {cleaned_text}. try to be relevant and answer to some vague questions also. If you cannot find anything in the context document try to generate it by yourself.
        If someone ask who are you then asnwer that you are the 'your onboarding buddy'.
         Act professional and freindly but be sweet as the same time."""
        
        # Using the generate_content method from the model instance
        response = model.generate_content([prompt])  # Use the model instance
        return response.text if hasattr(response, 'text') else "No response content found."
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return "An error occurred while generating the response."

def main():
    # File path to the cleaned text
    file_path = "C:/Users/mahan/OneDrive/Desktop/GenAIus/Preetha/AllCleanData/AllCleanData.txt"

    # Process the text and create the FAISS index
    logging.info("Processing cleaned data...")
    raw_text = get_clean_text(file_path)
    if raw_text is not None:
        logging.info("Text data loaded successfully.")
        
        # List available models
        logging.info("Listing available models...")
        list_available_models()

        # Generate embeddings for the cleaned data
        embeddings = generate_embeddings(raw_text)
        if embeddings is not None:
            logging.info("Embeddings generated successfully.")
        else:
            logging.error("Failed to generate embeddings.")
            return  # Exit if embedding fails
    else:
        logging.info("Failed to read cleaned text.")
        return  # Exit if reading text fails

    # Take user queries in the console
    while True:
        user_question = input("\nAsk a question from the cleaned data (or type 'exit' to quit): ")
        if user_question.lower() == 'exit':
            break
        answer = generate_response(user_question, raw_text)  # Pass cleaned text to the response function
        print("Reply from Gemini: ", answer)

if __name__ == "__main__":
    main()
