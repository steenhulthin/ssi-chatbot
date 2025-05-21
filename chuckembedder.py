from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import scraper

text = scraper.scrape_website("https://ssi.dk")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.create_documents([text])

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())