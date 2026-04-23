# 📄 RAG-based PDF Question Answering System

## 📌 Project Description

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that allows users to ask questions based on the content of PDF documents. It combines document retrieval with a language model to generate accurate and context-aware answers.

The system:

* Loads PDF documents
* Splits them into manageable chunks
* Converts text into embeddings
* Stores embeddings in a vector database (Chroma)
* Retrieves relevant context for queries
* Generates answers using a transformer-based LLM

---

## 🚀 Features

* 📂 Load multiple PDFs from a folder
* ✂️ Smart text chunking with overlap
* 🔍 Semantic search using embeddings
* 🧠 Context-aware answers using RAG
* ⚡ Lightweight and runs locally
* 🤖 Simple agent logic (direct vs search-based answers)

---

## 🛠️ Tech Stack

* Python
* LangChain
* HuggingFace Transformers
* ChromaDB (Vector Database)
* Sentence Transformers (Embeddings)

---

## 📁 Project Structure

```
.
├── data/                # Folder containing PDF files
├── main.py              # Main application script
└── README.md            # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/rag-pdf-qa.git
cd rag-pdf-qa
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add your PDFs

Place all your PDF files inside the `data/` folder.

---

## ▶️ Usage

Run the script:

```
python main.py
```

Then enter your query:

```
Enter your question: What is this document about?
```

Type `exit` to quit.

---

## 🧠 How It Works

### 1. Document Loading

PDF files are loaded using `PyPDFLoader`.

### 2. Text Chunking

Documents are split into smaller chunks using:

* Chunk size: 500
* Overlap: 80

### 3. Embeddings

Text chunks are converted into vector embeddings using:

```
all-MiniLM-L6-v2
```

### 4. Vector Store

Embeddings are stored in **ChromaDB** for efficient similarity search.

### 5. Retrieval

Top-k (k=3) relevant chunks are retrieved based on the query.

### 6. Generation

Answers are generated using:

```
google/flan-t5-base
```

### 7. Agent Controller

A simple rule-based controller decides:

* "search" → use RAG
* "direct" → answer without retrieval

---

## 📌 Example

**Input:**

```
Summarize the document
```

**Output:**

```
The document discusses...
```

---

## ⚠️ Limitations

* Simple keyword-based agent logic
* No persistent vector storage (data resets on rerun)
* Limited response length (max tokens = 150)

---

## 🔮 Future Improvements

* Add UI (Streamlit / React)
* Improve agent decision-making
* Use larger LLMs (e.g., LLaMA, GPT-based APIs)
* Add persistent database storage
* Support for other file formats (TXT, DOCX)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you like this project, give it a star ⭐ on GitHub!

---

# 🔖 GitHub Repository Description

**Short Description (one-line):**

> RAG-based PDF Question Answering system using LangChain, HuggingFace, and ChromaDB.

**Detailed Description:**

> This project implements a Retrieval-Augmented Generation (RAG) pipeline to answer user queries based on PDF documents. It uses LangChain for document processing, HuggingFace models for embeddings and text generation, and ChromaDB for vector storage. The system intelligently retrieves relevant document context and generates accurate answers using a transformer-based language model.
