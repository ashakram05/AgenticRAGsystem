import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline

import os

from transformers import pipeline
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"

# --------------------------
# Load PDFs
# --------------------------
def load_pdfs(folder_path):
    documents = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, file))
            documents.extend(loader.load())
    return documents

docs = load_pdfs("data")
print(f"Loaded {len(docs)} pages")

# --------------------------
# Chunking
# --------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=80
)
chunks = text_splitter.split_documents(docs)
print(f"Created {len(chunks)} chunks")

# --------------------------
# Embeddings
# --------------------------
print("Loading embedding model...")  # Helps to see progress
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    cache_folder="C:/Users/ashak/.cache/huggingface"
)

print("Embedding model loaded ✅")



# --------------------------
# Vector Store (Chroma)
# --------------------------
db = Chroma(
    collection_name="rag_store",
    embedding_function=embedding_model
)

# Add chunks to the DB
texts = [chunk.page_content for chunk in chunks]
db.add_texts(texts)

# Create retriever
retriever = db.as_retriever(search_kwargs={"k": 3})

print("Vector store created and chunks embedded ✅")


llm = pipeline(
    "text2text-generation",              
    model="google/flan-t5-base",
    max_new_tokens=150
)


def agent_controller(query):
    q = query.lower()
    if any(word in q for word in ["pdf", "document", "data", "summarize", "information", "find"]):
        return "search"
    return "direct"


def rag_answer(query):
    action = agent_controller(query)
    if action == "search":
        docs = retriever.invoke(query)
        context = "\n".join([doc.page_content for doc in docs])
        prompt = f"Use the following context to answer the question:\n{context}\nQuestion: {query}\nAnswer:"
    else:
        prompt = f"Answer the following question:\n{query}\nAnswer:"
    
    response = llm(prompt)
    return response[0]['generated_text']


# Example usage
while True:
    query = input("Enter your question: ")
    if query.lower() == "exit":
        break
    answer = rag_answer(query)
    print("Answer:", answer)