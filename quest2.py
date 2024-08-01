from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
import os
os.environ['FAISS_NO_AVX2'] = '1'
import requests
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain

os.environ['OPENAI_API_KEY'] = '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'


app = FastAPI()

# Configure CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class ResponseModel(BaseModel):
    title: str
    link_array: List[str]
    answer: str

def scrape_page_info(link):
   response = requests.get(link)
   soup = BeautifulSoup(response.content, 'html.parser')

   # Extract the title of the page
   title = soup.title.string if soup.title else "No Title Found"

   # Prepare a list of possible meta tag names
   possible_meta_tags = ['description', 'Keywords', 'keywords' ,'metadata']

   # Find and extract meta description (considering multiple tags)
   meta_description = None
   for tag_name in possible_meta_tags:
        meta_tag = soup.find('meta', attrs={'name': tag_name})
        if meta_tag:
            meta_description = meta_tag['content']
            break  # Exit the loop after finding a description

   # Handle case where no description is found
   meta_description = meta_description if meta_description else "No Meta Description Found"

   # Extract text content from each link
   link_soup = BeautifulSoup(requests.get(link).content, 'html.parser')
   link_paragraphs = link_soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
   link_page_text = ''
   for element in link_paragraphs:
        link_page_text += element.get_text(separator=' ', strip=True) + '\n'
   return {
      'title': title,
      'description': meta_description,
      'text_content': link_page_text,
      'url': link  # Include the URL as well
   }

@app.post("/search/", response_model=ResponseModel)
async def search():
    API_KEY = "AIzaSyBozBKoer2PI00pheCSXU2V8sNOgdT5urM"
    SEARCH_ENGINE_ID = "d27ac8cafeab74577"

    url = "https://www.googleapis.com/customsearch/v1"

    params = {
        'q' : 'what is computer science',
        'key' : API_KEY,
        'cx' : SEARCH_ENGINE_ID,
        'num' : 3
    }

    response = requests.get(url, params=params)
    results = response.json()

    links_array = []

    for item in results['items']:
        link = item['link']
        links_array.append(link)

    data = []  # Array to store website data
    text_documents = []

    # Scrape information for each retrieved link
    for link in links_array[:3]:
        website_data = scrape_page_info(link)
        data.append(website_data)

        # Extract the text content from the dictionary
        text_content = website_data['text_content']

        # Create a Document object with the extracted text
        document = Document(page_content=text_content)

        # Append the Document object to the text_documents list
        text_documents.append(document)

    llm = ChatOpenAI()
    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(text_documents)
    vectorstore = FAISS.from_documents(documents, embeddings)

    template = """Act as a search engine . answer the users query based on the context provided. with question demanding a definition and some other factors like importance, examples list; first define the term then if they requested for other thing like importance or example give them:
    <context>{context}</context>
    
    Query: {input}"""

    prompt = PromptTemplate.from_template(template)
    document_chain = create_stuff_documents_chain(llm, prompt)

    retriever = vectorstore.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    response = retrieval_chain.invoke({
        "input":  "What is computer science and give 3 importance?",
    })

    answer = response['answer']
    print(answer)

    return ResponseModel(
        title=", ".join([data['title'] for data in data]),
        link_array=links_array,
        answer=answer
    )
