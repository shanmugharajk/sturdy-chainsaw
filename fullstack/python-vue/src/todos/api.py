from fastapi import APIRouter
from fastapi.openapi.docs import get_redoc_html
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse

# Public routes
api_router = APIRouter(default_response_class=JSONResponse)


# doc routes
doc_router = APIRouter()


@doc_router.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return JSONResponse(
        get_openapi(
            title="Qanet Docs", servers=[{"url": "/api/v1"}], version=1, routes=api_router.routes
        )
    )


@doc_router.get("/", include_in_schema=False)
async def get_documentation():
    return get_redoc_html(openapi_url="/api/v1/docs/openapi.json", title="Qanet Docs")


api_router.include_router(doc_router, prefix="/docs")
