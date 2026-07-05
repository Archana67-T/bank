from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="BankGenius AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to BankGenius AI"
    }

@app.get("/banking")
def banking():
    return [
        {
            "title": "Reserve Bank of India",
            "content": "RBI is the Central Bank of India."
        },
        {
            "title": "Commercial Banks",
            "content": "Commercial banks accept deposits and provide loans."
        }
    ]

@app.get("/current-affairs")
def current_affairs():
    return [
        {
            "date": "2026-07-05",
            "news": "RBI announced new digital payment initiatives."
        },
        {
            "date": "2026-07-04",
            "news": "Banking sector reports improved loan growth."
        }
    ]

@app.get("/computer-awareness")
def computer():
    return [
        {
            "question": "What is CPU?",
            "answer": "Central Processing Unit"
        },
        {
            "question": "What is RAM?",
            "answer": "Random Access Memory"
        }
    ]

@app.get("/reasoning")
def reasoning():
    return [
        {
            "question": "Find the odd one: Apple, Mango, Banana, Car",
            "answer": "Car"
        }
    ]

@app.get("/aptitude")
def aptitude():
    return [
        {
            "question": "20 + 35 = ?",
            "answer": "55"
        }
    
