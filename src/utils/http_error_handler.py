from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from fastapi import FastAPI, Request, JSONResponse, Response, status


class http_error_handler(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            content = f"exc: {str(e)}"

            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

            return JSONResponse(content=content, status_code=status_code)