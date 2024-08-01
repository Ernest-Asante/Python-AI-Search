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

class CapitalInfo(BaseModel):
  answer: str = Field(description="The capital city name")
  source: str = Field(description="Source website for the answer")


response_schemas = [
    CapitalInfo.schema(),  # Capital of France (already has name and description)
    {"name": "answer", "description": "The capital city name for Germany"},  # Capital of Germany
    {"name": "source", "description": "Source website for the answer for Germany"},  # Capital of Germany
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
  template="For each of the following questions, answer as best as possible and provide the source of your answer.\n{format_instructions}\n1. What is the capital of France?\n2. What is the capital of Germany?",
  input_variables=["question"],
  partial_variables={"format_instructions": format_instructions},
)

chain = prompt | model | output_parser

result = chain.invoke({})  # No input question needed for this prompt

# No need to check for list type as output_parser guarantees an array
print(result)

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
    return result
