import os
from pymongo import MongoClient

# Connect to MongoDB
def connect_to_mongo(uri):
    client = MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error: {e}")
    return client

# Retrieve all documents from the collection
def retrieve_all_documents(collection):
    try:
        documents = collection.find()
        return list(documents)
    except Exception as e:
        print(f"Error while retrieving documents: {e}")
        return []

# Save files to local storage
def save_files_to_local(documents, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for doc in documents:
        filename = doc['filename']
        file_path = os.path.join(output_folder, filename)
        with open(file_path, 'wb') as file:
            file.write(doc['data'])  # Write the binary data
        print(f"Saved {filename} to {file_path}")

# Main function to download files
def download_files(uri, db_name, collection_name, output_folder):
    client = connect_to_mongo(uri)
    db = client[db_name]
    collection = db[collection_name]
    documents = retrieve_all_documents(collection)
    save_files_to_local(documents, output_folder)

# Example usage
if __name__ == "__main__":
    uri = "mongodb+srv://dibyajyoti:Password123@atlascluster.fi2qsez.mongodb.net/PROJECT0?retryWrites=true&w=majority"
    db_name = "Files"
    
    collections_and_folders = {
        "csv": r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\Downloads\csv",
        "docx": r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\Downloads\docx",
        "txt": r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\Downloads\txt",
        "json": r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\Downloads\json",
        "md": r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\Downloads\md",
        "pdf": r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\Downloads\pdf",
        "pptx": r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\Downloads\pptx",
        "png": r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\Downloads\png",
        "xlsx": r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\Downloads\xlsx"
    }
    
    for collection, folder in collections_and_folders.items():
        download_files(uri, db_name, collection, folder)
