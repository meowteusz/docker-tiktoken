from fastapi import FastAPI
import tiktoken
from pydantic import BaseModel

app = FastAPI()

class TokenRequest(BaseModel):
    text: str
    encoding_name: str = "cl100k_base"

@app.post("/count_tokens")
def count_tokens(request: TokenRequest):
    encoding = tiktoken.get_encoding(request.encoding_name)
    num_tokens = len(encoding.encode(request.text))
    return {"text": request.text, "tokens": num_tokens}
