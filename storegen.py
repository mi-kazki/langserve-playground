import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

load_dotenv()

DOCUMENTS_DIR_PATH = './docs'

vectorstore = FAISS.from_texts([""], OpenAIEmbeddings())
for filename in os.listdir(DOCUMENTS_DIR_PATH):
  loader = TextLoader(f'{DOCUMENTS_DIR_PATH}/{filename}') if filename.endswith('.txt') else PyPDFLoader(f'{DOCUMENTS_DIR_PATH}/{filename}')
  db = FAISS.from_documents(loader.load_and_split(), OpenAIEmbeddings())
  vectorstore.merge_from(db)

vectorstore.save_local("faiss_index")