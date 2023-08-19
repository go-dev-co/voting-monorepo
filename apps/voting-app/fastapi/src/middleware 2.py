from fastapi import HTTPException, Request


async def validate_user_hash_middleware(request: Request, call_next):
    x_user_hash = request.headers.get("X-User-Hash")

    if not x_user_hash:
        raise HTTPException(
            status_code=401, detail="Invalid submission: No unique user hash \
            provided")

    if len(x_user_hash) != 32:
        raise HTTPException(
            status_code=401, detail="Invalid submission: Unique user hash \
                invalid")

    response = await call_next(request)
    return response
