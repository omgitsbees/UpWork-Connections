import os
import json
import time
import logging
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from whoosh.analysis import StemmingAnalyzer
from transformers import pipeline
from getpass import getpass

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# User authentication
def authenticate_user():
    users = {
        "admin": "password123",  # Replace with a secure method of storing passwords
    }
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    if username in users and users[username] == password:
        logger.info("User authenticated successfully.")
        return True
    else:
        logger.error("Authentication failed.")
        return False

# Create index for files
def create_index(directory, index_dir):
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(analyzer=StemmingAnalyzer()))
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    ix = create_in(index_dir, schema)
    writer = ix.writer()

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):  # Index only text files for simplicity
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                writer.add_document(title=file, path=path, content=content)
    writer.commit()
    logger.info("Index created successfully.")

# Search files
def search_files(query_str, index_dir):
    ix = open_dir(index_dir)
    qp = QueryParser("content", ix.schema)
    q = qp.parse(query_str)

    with ix.searcher() as searcher:
        results = searcher.search(q, limit=10)
        for result in results:
            print(f"Title: {result['title']}, Path: {result['path']}")

# NLP query understanding
def get_query_intent(query):
    nlp = pipeline("zero-shot-classification")
    labels = ["search files", "other"]
    result = nlp(query, candidate_labels=labels)
    return result['labels'][0]

# Main chatbot function
def chatbot():
    if not authenticate_user():
        return

    print("Welcome to the Company File Search Chatbot!")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        intent = get_query_intent(query)
        if intent == "search files":
            search_files(query, "indexdir")
        else:
            print("Sorry, I can only help with searching files at the moment.")

if __name__ == "__main__":
    # Create index if it doesn't exist
    if not os.path.exists("indexdir"):
        create_index("path/to/company/files", "indexdir")

    # Run the chatbot
    chatbot()