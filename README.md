# LangChain Custom Chatbot 🚀

This project is a **custom chatbot** built using **LangChain**, designed to extract course data from [Brainlox](https://brainlox.com/courses/category/technical), generate embeddings, store them in a vector database, and serve responses via a **Flask REST API**.
### 🎯 **Final Step**: Push to GitHub
```bash
git add README.md
git commit -m "Added README"
git push origin main
```

Now you're **DONE! ✅** 🚀🔥 Let me know if you need any tweaks. 🎉

## 📌 Features
- **Web Scraping**: Extracts data from Brainlox using `WebBaseLoader`.
- **Vector Database**: Stores embeddings using `ChromaDB` for efficient retrieval.
- **Hugging Face Integration**: Uses `flan-t5-base` for answering user queries.
- **Flask API**: Provides a RESTful API to handle user queries (`/chat` endpoint).
- **Retrieval-Augmented Generation (RAG)**: Returns responses along with source documents.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Hindolch/langchain-demo.git
cd langchain-demo
```

### 2️⃣ Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add your Hugging Face API key:
```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
```

---

## 🚀 Usage

### 1️⃣ Run the Chatbot API
```bash
python app.py
```

### 2️⃣ Test API Using `curl`
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "How much do the programming courses cost?"}'
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/`     | Check if the API is running |
| `POST` | `/chat` | Query the chatbot |

### Example Request:
```json
{
  "query": "What courses are available?"
}
```
### Example Response:
```json
{
  "response": "Courses available include Python, Cloud Computing, and Scratch Programming.",
  "sources": [
    "Brainlox: Learn technical courses...",
    "Scratch Course is the foundation of coding..."
  ]
}
```

---

## 📜 Project Structure
```
📂 custom-chatbot-langchain
│-- 📜 scraper.py  # Extracts data from Brainlox
│-- 📜 vectorstore.py  # Embeds & stores data in ChromaDB
│-- 📜 app.py  # Flask API for chatbot
│-- 📜 requirements.txt  # Dependencies
│-- 📜 README.md  # Documentation
│-- 📜 .env  # API Keys (Ignored in Git)
```

---



## 📜 License
This project is licensed under the **MIT License**.

---


