from fastapi import FastAPI, APIRouter
from transcribinoff.routers import users_router

routers = [users_router]
root_router = APIRouter()
for router in routers:
    root_router.include_router(router)

app = FastAPI(
    title="TranscribinOff",
    description="TranscribinOff is a web application that allows users to transcribe audio files.",
    version="0.1.1",
)
app.include_router(root_router)
