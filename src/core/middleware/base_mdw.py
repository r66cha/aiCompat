"""Custom middleware for handling HTTP requests and responses."""

# -- Imports

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Callable, Awaitable


# --


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    """Middleware that processes incoming requests and outgoing responses."""

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ):
        """Handle request and response processing.

        Args:
            request (Request): Incoming HTTP request.
            call_next (Callable): Next handler in the middleware chain.

        Returns:
            Response: HTTP response returned by the application."""

        response: Response = await call_next(request)
        return response
