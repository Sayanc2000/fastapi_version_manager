from fastapi import FastAPI


def get_admin_handler(app: FastAPI):
    """
    Creates and returns an admin route handler for displaying FastAPI routes information.

    Args:
        app (FastAPI): The FastAPI application instance to extract routes from.

    Returns:
        callable: A route handler function that generates an HTML page displaying all routes.
    """
    def admin_route():
        """
        Generates an HTML page displaying all registered routes in the FastAPI application.

        Returns:
            str: An HTML document containing a formatted list of all routes, including their
                HTTP methods, paths, and names.
        """
        routes_html = ""
        for route in app.routes:
            methods = ", ".join(route.methods) if route.methods else "N/A"
            routes_html += f""" 
            <div style="border: 1px solid #ddd; margin: 10px 0; padding: 15px;">
                <div>
                    <span style="background: #eee; padding: 3px 8px; margin-right: 10px;">{methods}</span>
                    <span>{route.path}</span>
                </div>
                <div style="color: #666; margin-top: 5px;">Name: {route.name or 'N/A'}</div>
            </div>
            """

        return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>FastAPI Admin - Routes</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                </style>
            </head>
            <body>
                <h1>FastAPI Routes</h1>
                {routes_html}
            </body>
        </html>
        """

    return admin_route
