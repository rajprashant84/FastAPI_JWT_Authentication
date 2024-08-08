from fastapi import FastAPI
from app.routes import routes
from app.db.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes.router)
