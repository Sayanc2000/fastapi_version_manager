from fastapi import Request, HTTPException, status

def fix_version(request: Request, version: str = None):
    """
    TODO: Version would be later taken using centralised version manager class and fetched using path name and method
    """
    x_api_version = request.headers.get('X-Api-Version')
    if not x_api_version:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing required header: X-Api-Version")
    if version:
        if x_api_version != version:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="API version mismatch")
