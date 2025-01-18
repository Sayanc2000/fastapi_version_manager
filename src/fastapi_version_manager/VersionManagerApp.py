from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_version_manager.routes_functions import get_admin_handler


class ManagedApp(FastAPI):
    """A FastAPI application wrapper that adds version management capabilities.
    
    This class extends FastAPI to provide an administrative interface for managing
    API versions and documentation.
    
    Args:
        app (FastAPI): The main FastAPI application to be managed
        prefix (str, optional): URL prefix for the admin interface. Defaults to "/admin"
    """

    def __init__(self, app: FastAPI, prefix: str = "/admin"):
        super().__init__()
        self.app = app
        self.prefix = prefix
        self._setup_admin_route()

    def _setup_admin_route(self):
        """Configure the admin interface route.
        
        Sets up the administrative endpoint that provides the version management
        interface. This method is called automatically during initialization.
        """
        self.app.add_api_route(
            self.prefix,
            get_admin_handler(self.app),
            response_class=HTMLResponse,
        )
