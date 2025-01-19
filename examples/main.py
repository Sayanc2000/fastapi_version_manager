"""
FastAPI application with version management functionality.

This module implements a versioned REST API using FastAPI and fastapi_version_manager.
It defines multiple API versions with their respective metadata and provides basic endpoints.
"""

from fastapi import FastAPI

from fastapi_version_manager.version_manager_app import ManagedApp
from datetime import date
from fastapi_version_manager.api_version import VersionInfo
from fastapi import Request, Depends
from fastapi_version_manager.dependencies import fix_version
app = FastAPI()

"""
API versions defination example should be entirely handled in a version manager class
"""
versions = {
    "1.0": VersionInfo(
        version="1.0",
        released_date=date(2023, 1, 1),
        supported=True,
        deprecated=True,
        sunset_date=date(2024, 12, 31),
        description="Initial API version"
    ),
    "2.0": VersionInfo(
        version="2.0",
        released_date=date(2023, 6, 1),
        supported=True,
        description="Major update with breaking changes"
    ),
    "2.4": VersionInfo(
        version="2.4",
        released_date=date(2023, 9, 1),
        supported=True,
        description="Added advanced order management"
    ),
    "3.0": VersionInfo(
        version="3.0",
        released_date=date(2024, 1, 1),
        supported=True,
        description="Latest major version with enhanced features"
    )
}

ManagedApp(app, versions)

@app.get("/", dependencies=[Depends(fix_version)])
def read_root(version: str = None):
    # TODO: version would be fetched from version manager class
    """
    Root endpoint that returns a simple greeting message.

    Returns:
        dict: A dictionary containing a "Hello": "World" key-value pair
    """
    return {"Hello": "World"}
