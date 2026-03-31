from fastapi import FastAPI
from app.db.session import engine
from app.db import base

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/stocks/{symbol}")
async def read_stock(symbol: str):
    # Placeholder for stock data retrieval logic
    return {
        "symbol": symbol,
        "price": 100.0,
        "currency": "NGN"
        }

@app.get("/health/db")
async def check_db():
    try:
        with engine.connect() as conn:
            return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "details": str(e)}