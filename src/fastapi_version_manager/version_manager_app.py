from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import date
from typing import Dict

from fastapi_version_manager.routes_functions import get_admin_handler
from fastapi_version_manager.api_version import APIVersions, VersionInfo


class ManagedApp(FastAPI):
    """A FastAPI application wrapper that adds version management capabilities.
    
    This class extends FastAPI to provide an administrative interface for managing
    API versions and documentation.
    
    Args:
        app (FastAPI): The main FastAPI application to be managed
        prefix (str, optional): URL prefix for the admin interface. Defaults to "/admin"
    """

    def __init__(self, app: FastAPI, versions: Dict[str, VersionInfo], prefix: str = "/admin"):
        super().__init__()
        self.app = app
        self.prefix = prefix
        self._initialize_versions(versions)
        self._setup_admin_route()

    def _initialize_versions(self, versions: Dict[str, VersionInfo]):
        """Initialize API versions with their metadata."""
        
        APIVersions.initialize_versions(versions)

    def _setup_admin_route(self):
        """Configure the admin interface route.
        
        Sets up the administrative endpoint that provides the version management
        interface. This method is called automatically during initialization.
        """
        self.app.add_api_route(
            self.prefix,
            get_admin_handler(self.app, APIVersions.VERSIONS),
            response_class=HTMLResponse,
        )

    def _get_version_info(self, ver: str) -> VersionInfo:
        return APIVersions.get_version_info(ver)

    def _get_supported_versions(self) -> list[str]:
        return APIVersions.get_supported_versions()

    def _get_latest_version(self) -> str:
        return APIVersions.get_latest_version()
