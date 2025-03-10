from langchain.document_loaders import WebBaseLoader

url = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(url)
documents = loader.load()

for doc in documents:
    print(doc.page_content)  # Debugging to check extracted content
