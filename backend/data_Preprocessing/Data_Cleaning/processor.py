import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from the config/.env file
load_dotenv(dotenv_path="C:/Users/preet/Downloads/GenAIus/config/.env")

# Configure the Gemini API key using environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in the .env file.")

# Initialize the Gemini AI model
genai.configure(api_key=GEMINI_API_KEY)

# Function to clean/preprocess text using Gemini AI with batch processing
def clean_text_with_gemini(extracted_text):
    prompt = f"""
    Please clean and preprocess the following text by performing the following actions:
    - Remove unnecessary characters and symbols.
    - Correct any obvious typos.
    - Remove extra spaces and line breaks.
    - Ensure consistent formatting.
    - Retain all meaningful content related to company documentation, policies, and project information.
    - Give me only the raw and cleaned preview text of the cleansed data without any asterisk signs strictly.
    - Donot disobey the prompts at any cost!!!
    - Clean the following text by removing irrelevant symbols, correcting typos, and ensuring clarity while preserving essential information.
    Cleaned Text:
    {extracted_text}
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Retry mechanism for handling 429 errors
    while True:
        try:
            response = model.generate_content(prompt)
            cleaned_text = response.text.strip() if hasattr(response, 'text') else response.strip()
            return cleaned_text
        except Exception as e:
            if "Resource has been exhausted" in str(e):
                print("429 error encountered. Retrying in 10 seconds...")
                time.sleep(10)  # Wait before retrying
            else:
                raise e  # Raise other exceptions

# Function to process all chunk files in a directory
def process_all_chunks(input_dir):
    all_cleaned_text = ""

    # Iterate through each chunk file in the input directory
    for filename in os.listdir(input_dir):
        if filename.startswith("extracted_chunk") and filename.endswith(".txt"):
            chunk_file_path = os.path.join(input_dir, filename)
            with open(chunk_file_path, 'r', encoding='utf-8') as file:
                extracted_text = file.read()

            # Clean the chunk text using Gemini AI
            cleaned_chunk = clean_text_with_gemini(extracted_text)
            all_cleaned_text += cleaned_chunk + "\n"
            print(f"Processed {chunk_file_path}")

    # Append all cleaned text to the output file
    output_file = "C:/Users/preet/Downloads/GenAIus/Data Pre processing/all_cleaned_data.txt"
    with open(output_file, "a", encoding="utf-8") as outfile:
        outfile.write(all_cleaned_text)

    print("All chunks processed and appended to all_clean_data.txt")

# Example usage
input_dir = "C:/Users/preet/Downloads/GenAIus/Data Pre processing"
process_all_chunks(input_dir)
