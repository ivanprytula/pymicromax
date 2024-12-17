import highlight_io
import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from highlight_io.integrations.fastapi import FastAPIMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.config import settings


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(
        dsn=str(settings.SENTRY_DSN),
        environment=settings.ENVIRONMENT,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for tracing.
        traces_sample_rate=1.0,
        _experiments={
            # Set continuous_profiling_auto_start to True
            # to automatically start the profiler on when
            # possible.
            "continuous_profiling_auto_start": True,
        },
        enable_tracing=True,
    )

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

if settings.HIGHLIGHTIO_PROJECT_ID and settings.ENVIRONMENT != "local":
    import subprocess

    # Get the current Git SHA commit
    git_sha = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()

    # `instrument_logging=True` sets up logging instrumentation.
    # if you do not want to send logs or are using `loguru`, pass `instrument_logging=False`
    H = highlight_io.H(
        settings.HIGHLIGHTIO_PROJECT_ID,
        instrument_logging=True,
        service_name="backend-fastapi",
        service_version=git_sha,
        environment=settings.ENVIRONMENT,
    )
    app.add_middleware(FastAPIMiddleware)

# Set all CORS enabled origins
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
