import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

os.environ['OPENAI_API_KEY'] = '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'

model = ChatOpenAI()

response_schemas = [
    ResponseSchema(
        name="answer",
        description="answer to the user's question"),
    ResponseSchema(
        name="source",
        description="source used to answer the user's question, should be a website.",
    ),
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="answer the users question as best as possible.\n{format_instructions}\n{question}",
    input_variables=["question"],
    partial_variables={"format_instructions": format_instructions},
)

chain = prompt | model | output_parser

result = chain.invoke({"question": "what's the capital of france and that of germany?"})

#main = [result]
main = result if isinstance(result, list) else [result]

print(main)

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
   
    return  main