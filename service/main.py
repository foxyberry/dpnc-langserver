from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import asyncio
import os
import sys
sys.path.append(os.path.abspath("../lib"))
from env_loader import load_environment_variables
from file_utils import read_file


additional_env_vars = {"LANGCHAIN_PROJECT": "gra-web-test"}
env_vars = load_environment_variables('../.env', additional_vars=additional_env_vars)

### gpt
gpt = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0125")

# Load history and prompt template from text files
history_file = "../.prompt/history.txt"
prompt_file = "../.prompt/prompt.txt"

history = [read_file(history_file)]
prompt_template = read_file(prompt_file)
prompt = ChatPromptTemplate.from_template(prompt_template)
gpt_chain = prompt | gpt



async def generate_stream(input_data: dict):
    for chunk in gpt_chain.stream({"input": input_data, "history": history}):
        yield chunk.content


## web server 
app = FastAPI()


@app.post("/analyze/")
async def analyze_json(request: Request):
    input_data = await request.json()
    
    return StreamingResponse(generate_stream(input_data), media_type="text/plain")

