from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes import bedrock, java


def create_app() -> FastAPI:
    app = FastAPI(
        debug=False,
        title="MCPinger",
        version="1.0"
    )

    @app.get("/", include_in_schema=False, response_class=RedirectResponse, status_code=301)
    async def root():
        return "/docs"

    @app.get("/healthcheck", include_in_schema=False)
    async def get_healtcheck():
        return {
            "success": True,
            "message": "healthy"
        }

    app.include_router(bedrock.router)
    app.include_router(java.router)

    return app


app = create_app()