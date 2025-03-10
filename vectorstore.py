import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

from scraper import documents

# Load environment variables
load_dotenv()

# Set HuggingFace cache directory
os.environ['HF_HOME'] = os.path.join(os.getcwd(), 'hf_cache')

# Split text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Generate embeddings using a free model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = Chroma.from_documents(docs, embeddings)

# No need to call persist() as it's automatic now
print("Vector store created successfully.")