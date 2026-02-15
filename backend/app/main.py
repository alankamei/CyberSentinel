from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_logs import router as logs_router
from app.database.init_db import init_db

app = FastAPI(
    title="CyberSentinel API",
    description="Blue-Team Defensive Security Monitoring Platform",
    version="1.0.0"
)

@app.on_event("startup")
async def on_startup():
    await init_db()


# Allow frontend to connect later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(logs_router)
@app.get("/")
def root():
    return {"message": "CyberSentinel backend is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
