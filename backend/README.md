# GenAIus Backend Pipeline

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Data Extraction](#data-extraction)
- [Data Preprocessing](#data-preprocessing)
- [Training the GenAI Model](#training-the-genai-model)
- [Flask Backend](#flask-backend)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Setup](#environment-setup)
- [Contributing](#contributing)
- [License](#license)

## Overview
The backend pipeline for GenAIus is designed to handle the entire process of extracting data from multiple file formats, preprocessing the data, training the chatbot using Gemini AI, and deploying a Flask backend that connects to a Next.js frontend. This backend serves as the knowledge management engine for the chatbot.

## Project Structure
```bash
backend/
├── Data/
│   └── (Initial raw data of multiple formats)
├── DataChunks/
│   └── (Extracted data chunks from all_extracted_data.txt)
├── Downloads/
│   └── (Connected with MongoDB to download data)
├── AllCleanData.txt
├── ExtractedRawData.txt
├── app.py                 # Flask app connecting backend logic to the frontend
├── cleaningChunks.py      # Splits large datasets into smaller chunks
├── downloadRawFiles.py    # Downloads raw files from MongoDB
├── embeddings.json        # Vector embeddings for the Gen AI model
├── environment.yml        # Environment configuration (API keys, directory paths, etc.)
├── extractor.py           # Extracts text data from various file formats
├── model.py               # Handles the model training and inference
├── ScrapeHTML.py          # Scrapes text data from HTML web pages
├── splittingDataToChunks.py  # Splits large datasets into smaller chunks
└── uploadRawFiles.py      # Uploads raw files to the backend
```

## Data Extraction
The data extraction process involves collecting text data from a variety of file formats, including .pdf, .docx, .csv, .pptx, .json, .html, and image-based text using OCR.

*Libraries Used:*
os: To manage file system operations.
docx: For reading .docx files.
csv: For parsing .csv files.
openpyxl: For working with .xlsx files.
selenium: For web scraping, specifically extracting content from HTML pages.
pytesseract: For optical character recognition (OCR) on image files.
PyPDF2: For reading and extracting text from .pdf files.
cv2 (OpenCV): To process image files for text recognition.
pptx: To extract text from PowerPoint presentations (.pptx).

Scripts:
extractor.py: Extracts text data from various file formats using the libraries mentioned above.
ScrapeHTML.py: Extracts text data from HTML web pages via Selenium automation.

## *Data Preprocessing*
Once the data is extracted, it undergoes preprocessing for cleaning and structuring. The preprocessing pipeline ensures that the data is fed efficiently into the Gemini AI model.

*Data Cleaning:*
In the Data_Cleaning subfolder, the extracted data is split into smaller chunks for efficient processing.

*splitting_data_to_chunks.py:* Breaks down the large dataset into manageable pieces.

*Data Processing:*
*processor.py:* Sends data chunks to the Gemini AI model for cleaning and processing. The processed data is saved into all_cleaned_data.txt.

## Training the GenAI Model
QueryFile.py contains the logic for training and fine-tuning the chatbot's model. Using Gemini AI's Embeddings API (specifically the models/text-embedding-004), we generate vector embeddings for the text data.

Logic:
User inputs a query.
The query is transformed into embeddings using the Gemini AI model.
A search is conducted through the database to retrieve relevant responses.
The response is returned to the user.

## Flask Backend
The Flask backend serves as the connection point between the front-end and the logic embedded in the QueryFile.py. It handles requests, sends queries to the AI model, and delivers responses.

*app.py*
The app.py script sets up the Flask app and handles HTTP requests using GET and POST methods. It routes the data to the frontend and ensures secure communication with the chatbot.

*Libraries Used:*
Flask
Flask-CORS (Cross-Origin Resource Sharing)
dotenv (for environment variable management)
Google Generative AI SDK (for using Gemini AI)
markdown (for rendering markdown content)

## Installation
To set up the backend, follow these steps:

1. *Clone the repository:*
    git clone https://github.com/Pree-04/Team-GenAIus
    cd GenAIus/backend

2. *Install dependencies:*
    pip install -r requirements.txt

3. *Important:*
    After cloning or forking the project, make sure to change the directories and paths in the code to reflect your respective local paths where you have saved the project files.

## Usage
To run the backend:
The Flask server should now be running on http://localhost:5000.

## Environment Setup
Ensure you have created a .env file in the backend directory with the following environment variables:

GEMINI_API_KEY: Your Gemini AI API key for cleaning and processing the data.
Other Variables: Replace any directory paths with your system's local paths to point to the correct file locations.
*For example:*
GEMINI_API_KEY=your_gemini_api_key_here
DATA_DIRECTORY=/path/to/your/data

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
