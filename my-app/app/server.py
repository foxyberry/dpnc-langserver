#!/usr/bin/env python
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatAnthropic
from langserve import add_routes
import asyncio
import os
import sys

sys.path.append(os.path.abspath("../lib"))
from env_loader import load_environment_variables
from file_utils import read_file

additional_env_vars = {"LANGCHAIN_PROJECT": "gra-web-test"}
env_vars = load_environment_variables('../.env', additional_vars=additional_env_vars)


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

gpt = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0125")


prompt_file = "../.prompt/prompt.txt"

prompt_template = read_file(prompt_file)
prompt = ChatPromptTemplate.from_template(prompt_template)
gpt_chain = prompt | gpt

add_routes(
    app,
    gpt_chain,
    path="/analyze"
)

async def generate_stream(input_data: dict):
    for chunk in gpt_chain.stream({"input_data": input_data}):
        yield chunk.content


@app.post("/analyze/")
async def analyze_json(request: Request):
    input_data = await request.json()
    return StreamingResponse(generate_stream(input_data), media_type="text/plain")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8123)