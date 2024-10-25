# GenAIus KT: Knowledge Management System

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Pipeline Overview](#pipeline-overview)
- [Data Collection](#data-collection)
- [Data Extraction](#data-extraction)
- [Data Preprocessing](#data-preprocessing)
- [Training the Gen AI Model](#training-the-gen-ai-model)
- [Flask Backend](#flask-backend)
- [Frontend with Next.js](#frontend-with-nextjs)
- [Installation](#installation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Overview
GenAIus KT is a Q&A chatbot designed for knowledge management within a company. It assists employees, especially new interns and trainees, in understanding ongoing and previous projects. The chatbot responds to queries related to educational content and project details, making knowledge transfer seamless and efficient.

## Project Structure
```bash
GenAIus/
├── backend/
│   ├── Data/
│   │   └── (Initial raw data of multiple formats)
│   ├── DataChunks/
│   │   └── (Extracted data chunks from all_extracted_data.txt)
│   ├── Downloads/
│   │   └── (Connected with MongoDB to download data)
│   ├── AllCleanData.txt
│   ├── ExtractedRawData.txt
│   ├── app.py
│   ├── cleaningChunks.py
│   ├── downloadRawFiles.py
│   ├── embeddings.json
│   ├── environment.yml
│   ├── extractor.py
│   ├── model.py
│   ├── ScrapeHTML.py
│   ├── splittingDataToChunks.py
│   └── uploadRawFiles.py
├── frontend/
│   └── (Next.js files)
├── README.md 
└── LICENSE
```

## Pipeline Overview
The pipeline for the GenAIus chatbot consists of several steps:

1. **Data Collection**: Gathering company data from various file formats.
2. **Data Extraction**: Extracting textual data using Python libraries.
3. **Data Preprocessing**: Cleaning and structuring the extracted data using the Gemini AI model.
4. **Training the Gen AI Model**: Creating vector embeddings and training the chatbot.
5. **Flask Backend**: Setting up the backend for handling requests.
6. **Frontend Development**: Building a user-friendly interface using Next.js.

## Data Collection
The first step in the pipeline involves collecting data from various company documents, including:

- PDF
- DOC/DOCX
- Google Docs (.gdoc)
- XLS/XLSX
- Google Sheets
- PPT/PPTX
- Google Slides
- JPG/PNG
- SVG
- CSV
- Markdown (MD)
- TXT/JSON/XML
- HTML

Since company data is often confidential, dummy but realistic data has been created in these formats.

## Data Extraction
Textual data extraction is performed using several Python libraries, which read the contents of various file formats and save them to a consolidated text file (`ExtractedRawData.txt`). The libraries used include:

- `os`
- `docx`
- `csv`
- `openpyxl`
- `PyPDF2`
- `cv2`
- `pytesseract`
- `pptx`
- `selenium` (for web-based data)

## Data Preprocessing
The extracted textual data is preprocessed using the Google Gemini AI model. Given the large dataset, the data is chunked into smaller pieces and processed in batches. The cleaned data is saved into a file called `AllCleanData.txt`.

### Important: Gemini API Key
The project utilizes the Gemini API key for the data cleaning and training parts. After cloning or forking the project, make sure to replace the placeholder in the `.env` file with your own Gemini API key.

## Training the Gen AI Model
Once the data is cleaned, the next step is creating vector embeddings using the Gemini AI model. The chatbot uses these embeddings to retrieve relevant information based on user queries, ensuring it remains focused on its domain.

## Flask Backend
The Flask backend is responsible for connecting the frontend to the chatbot's processing logic. The backend handles requests and responses between the user interface and the AI model.

## Frontend with Next.js
The user interface is built using Next.js, providing a user-friendly chat interface for employees to interact with the GenAIus chatbot. The frontend design emphasizes accessibility and ease of use.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Pree-04/Team-GenAIus
   cd GenAIus

2. Important: After cloning or forking the project, make sure to change the directories and paths in the code to reflect your respective local paths where you have saved the project files.
   
3. Install backend dependencies:
   cd backend
   pip install -r requirements.txt

4. Set up the frontend:
   cd frontend
   npm install

5. Create a .env file in the backend directory and add your Gemini API key:
   GEMINI_API_KEY=your_gemini_api_key_here

## Usage
To run the backend server:
cd backend
python app.py

To start the frontend:
cd frontend
npm run dev

Visit http://localhost:3000 to interact with the chatbot.

## Future Improvements
**End-to-End Integration:** Fully deploy the web application with comprehensive integration of the chatbot to enhance its accessibility.
**Hierarchical Access Control:** Implement a feature that restricts access to confidential data based on the employee's position within the organization. This ensures that sensitive information is only accessible to those with the appropriate clearance.

## Contributing
Contributions are welcome! Please create a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

