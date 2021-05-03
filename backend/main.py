from fastapi import FastAPI, Request
import uvicorn
from typing import Optional
from pydantic import BaseModel


class Processor_text(BaseModel):
    text: str
    description: Optional[str] = None


class Report_text(BaseModel):
    text: str
    description: Optional[str] = None


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the Quado API root API"}


@app.post("/process_text/")
async def process_text(text: Processor_text):
    return text # {"message": " posted to the text processor API"}


@app.post("/generate_report/")
async def generate_report(text: Report_text):
    return text # {"message": "posted to the report generator API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)