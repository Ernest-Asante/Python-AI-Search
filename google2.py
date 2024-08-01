import os
os.environ['FAISS_NO_AVX2'] = '1'
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain



loader = WebBaseLoader("https://www.biologyonline.com/dictionary/biology")

docs = loader.load()

print(docs)

os.environ['OPENAI_API_KEY'] = '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'

llm = ChatOpenAI()

embeddings = OpenAIEmbeddings()


text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vectorstore = FAISS.from_documents(documents, embeddings)

template = """Act as a search engine . answer the users query based on the context provided:
<context>{context}</context>

Query: {input}"""

prompt = PromptTemplate.from_template(template)
document_chain = create_stuff_documents_chain(llm, prompt)

result = document_chain.invoke({
    "input": "What is biology?",
    "context": [Document(page_content= "biology is life science")]
})




retriever = vectorstore.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({
      "input": "What is biology and give 3 important?",
})

print(response['answer'])
