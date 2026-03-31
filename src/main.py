from fastapi import FastAPI
from sqlalchemy import text

from src.api.routes import stop
from src.core.database import Base, engine
from src import models 

app = FastAPI()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API running 🚀"}


@app.get("/test-db")
def test_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {
            "status": "connected",
            "result": [row[0] for row in result]
        }
    


# Including Routes
app.include_router(stop.router)