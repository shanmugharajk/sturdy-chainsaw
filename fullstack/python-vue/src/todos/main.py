from fastapi import FastAPI

from .api import api_router

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/")
def read_root():
    """dummy route to serve in the base url"""
    return {"Message": "Hey, sherlock!"}


# we add all API routes to the Web API framework
app.include_router(api_router, prefix="/api/v1")
