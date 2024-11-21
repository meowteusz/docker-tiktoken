from fastapi import FastAPI
import tiktoken
from pydantic import BaseModel

app = FastAPI()

class TokenRequest(BaseModel):
    text: str
    encoding: str

@app.post("/count_tokens")
def count_tokens(request: TokenRequest):
    encoding = tiktoken.get_encoding(request.encoding)
    num_tokens = len(encoding.encode(request.text))
    return {"text": request.text, "encoding": request.encoding, "tokens": num_tokens}
