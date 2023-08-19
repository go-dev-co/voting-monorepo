from fastapi import FastAPI, HTTPException
from src.middleware import validate_user_hash_middleware
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

# Vote post request, should contain a json body with a unique user hash key
# and a value of either cats or dogs


@app.post("/vote")
async def post_vote(item_data: dict):

    if item_data["vote"] == "dogs":
        # Submit vote to redis
        return {"vote": "dogs"}
    if item_data["vote"] == "cats":
        # Submit vote to redis
        return {"vote": "cats"}
    else:
        raise HTTPException(status_code=401, detail="Invalid submission")

# Register Middleware
app.middleware("http")(validate_user_hash_middleware)
