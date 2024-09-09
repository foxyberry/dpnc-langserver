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

# 경로 추가
sys.path.append(os.path.abspath("../lib"))
from env_loader import load_environment_variables
from file_utils import read_file

# 환경 변수 로드
additional_env_vars = {"LANGCHAIN_PROJECT": "gra-web-test"}
env_vars = load_environment_variables('../.env', additional_vars=additional_env_vars)


# FastAPI 앱 생성
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)
# GPT 모델 설정 (gpt-3.5-turbo-0125)
gpt = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0125")
# 프롬프트 및 히스토리 로드
history_file = "../.prompt/history.txt"
prompt_file = "../.prompt/prompt.txt"

history = [read_file(history_file)]
prompt_template = read_file(prompt_file)
prompt = ChatPromptTemplate.from_template(prompt_template)
gpt_chain = prompt | gpt

add_routes(
    app,
    gpt_chain,
    path="/analyze"
)

async def generate_stream(input_data: dict):
    for chunk in gpt_chain.stream({"input": input_data, "history": history}):
        yield chunk.content


@app.post("/analyze/")
async def analyze_json(request: Request):
    input_data = await request.json()
    return StreamingResponse(generate_stream(input_data), media_type="text/plain")



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8123)