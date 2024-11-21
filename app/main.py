from fastapi import FastAPI
import tiktoken
from pydantic import BaseModel
from typing import Literal

app = FastAPI(
    title="Token Counter API",
    description="Count tokens in text strings using variable encodings",
    version="1.0.0"
)

class TokenRequest(BaseModel):
    text: str
    encoding: Literal["o200k_base", "cl100k_base", "p50k_base", "r50k_base"] = "cl100k_base"

    model_config = {
        "schema_extra": {
            "examples": [
                {
                    "text": "An example string to tokenize.",
                    "encoding": "cl100k_base"
                }
            ]
        }
    }

class TokenResponse(BaseModel):
    text: str
    encoding: Literal["o200k_base", "cl100k_base", "p50k_base", "r50k_base"]
    tokens: int

    model_config = {
        "schema_extra": {
            "examples": [
                {
                    "text": "An example string to tokenize.",
                    "encoding": "cl100k_base",
                    "tokens": 5
                }
            ]
        }
    }

@app.post("/count", response_model=TokenResponse)
def count_tokens(request: TokenRequest):
    """
    Count tokens in a given string using a specified encoding.
    """
    encoding = tiktoken.get_encoding(request.encoding)
    num_tokens = len(encoding.encode(request.text))
    return TokenResponse(text=request.text, encoding=request.encoding, tokens=num_tokens)