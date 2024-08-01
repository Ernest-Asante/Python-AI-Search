import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field

os.environ['OPENAI_API_KEY'] = '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'

model = ChatOpenAI()

# Define your desired data structure.
class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

# And a query intented to prompt a language model to populate the data structure.
joke_query = "Tell me 5 jokes."

# Set up a parser + inject instructions into the prompt template.
parser = JsonOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

all_jokes = chain.invoke({"query": joke_query})

jokes =  all_jokes

#jokes = all_jokes if isinstance(all_jokes, list) else [all_jokes]

print(jokes)
