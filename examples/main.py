from fastapi import FastAPI

from fastapi_version_manager.VersionManagerApp import ManagedApp

app = FastAPI()

ManagedApp(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def test_route():
    return {
        "path": "new path",
    }
