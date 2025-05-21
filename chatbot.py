from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import chuckembedder

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    retriever=chuckembedder.vectorstore.as_retriever()
)

response = qa.run("What is this site about?")
print(response)