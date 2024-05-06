from fastapi import APIRouter, Depends, HTTPException
from app.oauth import get_github_oauth_url, exchange_code_for_token, get_github_user
from app.auth import create_access_token

router = APIRouter()

@router.get("/auth/github/login")
async def github_login():
    url = await get_github_oauth_url()
    return {"url": url}

@router.get("/auth/github/callback")
async def github_callback(code: str):
    try:
        access_token = await exchange_code_for_token(code)
        user_data = await get_github_user(access_token)
        
        # TODO: Create or update user in database
        
        jwt_token = create_access_token(
            data={"sub": user_data["id"], "email": user_data["email"]}
        )
        
        return {
            "access_token": jwt_token,
            "token_type": "bearer",
            "user": {
                "id": user_data["id"],
                "login": user_data["login"],
                "email": user_data.get("email")
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
