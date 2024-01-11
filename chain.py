from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

load_dotenv()

db = FAISS.load_local("./faiss_index", OpenAIEmbeddings())

chain = ConversationalRetrievalChain.from_llm(ChatOpenAI(), db.as_retriever())