import asyncio
from typing import TypeVar

from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from hypercorn.asyncio import serve as hypercorn_server
from hypercorn.config import Config as HypercornConfig
from hypercorn.typing import ASGIFramework

from test_task_urlencode.routes import router


ServiceApp = TypeVar("ServiceApp", ASGIFramework, FastAPI)
app = FastAPI(title="URL-encode service")


def build_app() -> ServiceApp:
    app.include_router(router)

    versioned_app = VersionedFastAPI(
        app=app,
        version_format="{major}",
        prefix_format="/api/v{major}",
    )

    return versioned_app


def run() -> None:
    asyncio.run(
        hypercorn_server(
            app=build_app(),
            config=HypercornConfig()
        )
    )
