from fastapi import FastAPI
from src.core.database import engine
from sqlalchemy import text


app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running 🚀"}


@app.get("/test-db")
def test_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"status": "connected", "result": [row[0] for row in result]}