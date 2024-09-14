#!/usr/bin/env python
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import os
import sys
sys.path.append(os.path.abspath("../lib"))
from env_loader import load_environment_variables
from file_utils import read_file
from auth import jwt_middleware

additional_env_vars = {"LANGCHAIN_PROJECT": "python-graph-test"}

environment = os.getenv("ENVIRONMENT", "local")
print(f"===================> environment: {environment}")

if environment == "prod":
    load_environment_variables('./.env.prod', additional_vars=additional_env_vars)
elif environment == "test":
    load_environment_variables('./.env.test', additional_vars=additional_env_vars)
else:
    load_environment_variables('./.env.local', additional_vars=additional_env_vars)

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)
app.middleware("http")(jwt_middleware)

gpt = ChatOpenAI(temperature=0, model="gpt-4o-mini")

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
    if environment == "prod":
        ssl_keyfile =  '../certs/key.pem' 
        ssl_certfile = '../certs/cert.pem'

        print(f"SSL Keyfile: {ssl_keyfile}")
        print(f"SSL Certfile: {ssl_certfile}")

        uvicorn.run(app, host="0.0.0.0", port=8123,
                    ssl_keyfile=ssl_keyfile,
                    ssl_certfile=ssl_certfile)
    else:
        uvicorn.run(app, host="0.0.0.0", port=8123)