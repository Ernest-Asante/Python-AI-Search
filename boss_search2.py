from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import json

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


def scrape_page_info(link):
   response = requests.get(url)
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


url = "https://www.googleapis.com/customsearch/v1"



def process_query() -> str:
    """Processes the query, retrieves information, and returns the response."""

    # ... (Search engine API call and link retrieval)

    API_KEY = "AIzaSyBozBKoer2PI00pheCSXU2V8sNOgdT5urM"
    SEARCH_ENGINE_ID = "d27ac8cafeab74577"

    search_guery = "machine learning roadmap "

    url = "https://www.googleapis.com/customsearch/v1"

    params = {
    'q' : search_guery,
    'key' : API_KEY, 
    'cx' : SEARCH_ENGINE_ID,
    'num' : 2
   # 'searchType' : 'image'
   }

    response = requests.get(url, params = params)
    results = response.json()


    links_array = []


    for item in results['items']:
     link = item['link']
     print(link)
     links_array.append(link)
    # Join links with commas and store in a new variable
    all_links = ", ".join(links_array)
    print(all_links)
    print(links_array)

    docs = ""
 

    # Scrape information for each retrieved link
    data = []
    text_documents = []
    for link in links_array[:2]:
        website_data = scrape_page_info(link)  # Call the scrape function here
        data.append(website_data)
        text_content = website_data['text_content']
        document = Document(page_content=text_content)
        text_documents.append(document)

    # ... (Rest of the LLM and retrieval chain processing)
        print(data)  # Now data conta

    llm = ChatOpenAI()

    embeddings = OpenAIEmbeddings()


    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(text_documents)
    vectorstore = FAISS.from_documents(documents, embeddings)

    template = """Act as a search engine . answer the users query based on the context provided. with question demanding a definition and some other factors like importance, examples list; first define the term briefly or give a brief explanation when the question demands explanation then if they requested for other thing like importance or example give them:
    <context>{context}</context>

    Query: {input}"""

    prompt = PromptTemplate.from_template(template)
    document_chain = create_stuff_documents_chain(llm, prompt)

   #result = document_chain.invoke({
   #    "input": "What is biology?",
   #    "context": [Document(page_content= "biology is life science")]
   #})




    retriever = vectorstore.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)


    response = retrieval_chain.invoke({"input": "Generate a detailed machine learning roadmap as a list of topics and skills to be learned sequentially. Each item in the list should be a concise point that describes a step or topic necessary for progressing in machine learning, starting from beginner to advanced levels. Generate a JSON response containing a list of courses where each course has a name, and description. The JSON response should be your output format. The name of the main json object should be machine_learning", })
    """"if isinstance(response['answer'], str):
    
     try:
        # Attempt to parse the string back to a list if it's not already
        topics_list = json.loads(response['answer'])
     except json.JSONDecodeError:
        print("Error: The response is not in valid JSON format.")
        topics_list = []
    else:
     topics_list = response['answer']"""

  
    print( response['answer'])
    return {'response': response['answer'], 
            
            
    }

app = FastAPI() 

origins = ["*"]  # Allow requests from your React frontend

app.add_middleware(
    CORSMiddleware,  
    allow_origins=origins, 
    allow_credentials=True,  # Allow cookies if needed
    allow_methods=["*"],  # Allow all HTTP methods (adjust as needed)
    allow_headers=["*"],  # Allow all headers (adjust as needed)
)

@app.get("/answer")
async def get_answer():
   
    answer = process_query()
    return {"response": answer} 


