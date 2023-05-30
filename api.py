from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from llama_cpp import Llama
import os

# print(os.listdir('./models'))
llm = Llama("./models/gpt4-x-vicuna-13B.ggmlv3.q5_1.bin")

# gptj = GPT4All("./models/gpt4-x-vicuna-13B.ggmlv3.q5_1.bin")
# model = Model(model_path='/home/cuya/Projects/ml-projects/gpt4all-ui/models/gpt4-x-vicuna-13B.ggmlv3.q5_1.bin')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        '*'
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/send_message')
async def send_message(request: Request):
    request_data = await request.json()
    message = request_data['message']
    output = llm(f"Q: {message} A: ", max_tokens=60, stop=["Q:", "\n"], echo=True)
    answer = output["choices"][0]['text'].split(' A: ')[1]
    return {'answer': answer}