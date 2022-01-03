from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import screenshot

app = FastAPI(docs_url=None, redoc_url="/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(screenshot.router, prefix="/api")

app.mount("/screenshots", StaticFiles(directory="screenshots"), name="screenshots")
app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="frontend")
