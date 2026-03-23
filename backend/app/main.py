from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.routes import tasks
import time
import uvicorn

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 IMPORTANT : attendre que la DB soit prête
time.sleep(5)

# Création des tables
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(tasks.router)

if __name__ == "__main__":
    # host="0.0.0.0" pour que FastAPI soit accessible depuis Kubernetes
    uvicorn.run(app, host="0.0.0.0", port=8000)

