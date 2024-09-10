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


gpt = ChatOpenAI(temperature=0, model="gpt-4o-mini")
#gpt = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0125")
#gpt = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")


pyeong_prompt_file = "../.prompt/pyeong_price_prompt.txt"
land_prompt_file = "../.prompt/land_price_prompt.txt"


add_routes(
    app,
    ChatPromptTemplate.from_template(read_file(pyeong_prompt_file)) | gpt,
    path="/pyeong-analyze"
)

add_routes(
    app,
    ChatPromptTemplate.from_template(read_file(land_prompt_file)) | gpt,
    path="/landprice-analyze"
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8123)