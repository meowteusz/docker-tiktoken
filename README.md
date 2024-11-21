# Token Counter API

A FastAPI service that counts tokens in text strings using OpenAI's `tiktoken`
library. Supports multiple encodings.

## Features

- REST API endpoint for token counting
- Configurable encoding schemes
- OpenAPI documentation (Swagger UI)
- Docker and Docker Compose support

## Quick Start

```bash
# Run with Docker Compose
docker-compose up --build

# Or build and run Docker manually
docker build -t token-counter .
docker run -p 8000:8000 token-counter
```

## API Usage

### Swagger UI Documentation

Access the interactive API documentation at `http://localhost:8000/docs`

### Count Tokens

```bash
curl -X POST "http://localhost:8000/count_tokens" \
-H "Content-Type: application/json" \
-d '{
    "text": "Hello, world!",
    "encoding": "cl100k_base"
}'
```

Response:

```json
{
    "text": "Hello, world!",
    "encoding": "cl100k_base",
    "tokens": 4
}
```

### Available Encodings

- o200k_base: For gpt-4o, gpt-4o-mini 
- cl100k_base: For gpt-4-turbo, gpt-4, gpt-3.5-turbo, text-embedding-ada-002, text-embedding-3-small text-embedding-3-large 
- p50k_base: For Codex models, text-davinci-002, text-davinci-003 
- r50k_base (or gpt2): For GPT-3 models like davinci

## Requirements

- Docker
- Docker Compose (optional)

## Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run locally: `uvicorn main:app --reload`
