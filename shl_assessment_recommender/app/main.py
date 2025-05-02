from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from app.model import recommend

app = FastAPI()
df = pd.read_csv("app/shl_catalog.csv")

class QueryRequest(BaseModel):
    query: str
    duration_limit: int = 90

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/recommend")
def recommend_tests(req: QueryRequest):
    return recommend(req.query, req.duration_limit)
