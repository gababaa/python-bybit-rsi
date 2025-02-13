from httpx import AsyncClient


async def make_request(
    url: str,
    method: str,
    params: dict | None = None,
    body: dict | None = None,
) -> dict:
    """Make simple http requests.

    Args:
        url: api url.
        method: request method.
        params: request params.
        body: request body.

    Returns:
        json response: dict.
    """
    async with AsyncClient() as client:
        response = await client.request(
            url=url,
            method=method,
            params=params,
            json=body,
        )
        return response.json()