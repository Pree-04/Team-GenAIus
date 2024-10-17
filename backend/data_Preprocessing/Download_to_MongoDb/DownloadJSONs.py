import os
from pymongo import MongoClient

# Step 1: Connect to MongoDB Cluster
def connect_to_mongo(uri):
    client = MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error: {e}")
    return client

# Step 2: Function to retrieve all PDF documents from the collection
def retrieve_all_pdfs(collection):
    try:
        # Retrieve all documents from the collection
        pdf_documents = collection.find()  # Fetch all PDFs
        return list(pdf_documents)  # Convert cursor to list
    except Exception as e:
        print(f"Error while retrieving documents: {e}")
        return []

# Step 3: Function to save PDFs to local storage
def save_pdfs_to_local(pdf_documents, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output folder if it doesn't exist
    
    for doc in pdf_documents:
        filename = doc['filename']
        file_path = os.path.join(output_folder, filename)
        with open(file_path, 'wb') as pdf_file:
            pdf_file.write(doc['data'])  # Write the binary data to a file
        print(f"Saved {filename} to {file_path}")

# Example usage
if __name__ == "__main__":
    # MongoDB connection URI
    uri = "mongodb+srv://dibyajyoti:Password123@atlascluster.fi2qsez.mongodb.net/PROJECT0?retryWrites=true&w=majority"

    # Connect to MongoDB and select the 'Files' database
    client = connect_to_mongo(uri)
    db = client["FIles"]

    # Access the 'pdfs' collection
    pdfs_collection = db["JSONs"]

    # Retrieve all PDF documents from the collection
    pdf_documents = retrieve_all_pdfs(pdfs_collection)

    # Folder to save the retrieved PDFs
    output_folder = "C:/Users/mahan/OneDrive/Desktop/GenAIus/downloadFiles/JSONs"  # Specify your desired output path

    # Save all retrieved PDFs to local storage
    save_pdfs_to_local(pdf_documents, output_folder)
