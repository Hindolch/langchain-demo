from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFaceHub
import os
from dotenv import load_dotenv
from vectorstore import vectorstore

# Load environment variables
load_dotenv()

# Set HuggingFace cache directory to current working directory
os.environ['HF_HOME'] = os.path.join(os.getcwd(), 'hf_cache')

app = Flask(__name__)
api = Api(app)

# Ensure API key is set
if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
    raise ValueError("HUGGINGFACEHUB_API_TOKEN environment variable is not set")

# Load Retrieval Chain with HuggingFaceHub instead of HuggingFaceEndpoint
llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    model_kwargs={
        "temperature": 0.5,
        "max_length": 250
    }
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# Add a root route
@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "endpoints": {
            "chat": "/chat (POST)",
        }
    })

class Chatbot(Resource):
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return {"error": "No JSON data provided"}, 400
            
            query = data.get("query")
            if not query:
                return {"error": "Query not provided"}, 400
            
            # Use invoke instead of run and convert response to string
            response = qa_chain.invoke(query)
            
            # Extract the answer and sources
            if isinstance(response, dict):
                answer = response.get('result', '')
                sources = [doc.page_content for doc in response.get('source_documents', [])]
                return {
                    "response": answer,
                    "sources": sources[:2]
                }
            else:
                return {"response": str(response)}
        
        except Exception as e:
            return {"error": str(e)}, 500

api.add_resource(Chatbot, "/chat")

if __name__ == "__main__":
    app.run(debug=True)
