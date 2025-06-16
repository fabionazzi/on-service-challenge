from fastapi import FastAPI
from on_service.interfaces.api.v1.endpoints.journey import router as journey_router

app = FastAPI()
app.include_router(journey_router)
