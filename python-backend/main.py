from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your Chrome extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for local dev; tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "PPOOOPPPPP!"}
