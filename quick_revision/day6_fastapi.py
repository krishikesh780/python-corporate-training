"""
Quick Revision — Day 6: FastAPI (optional)
============================================
Install: pip install fastapi uvicorn

Run API:
  cd quick_revision
  uvicorn day6_fastapi:app --reload

Docs: http://127.0.0.1:8000/docs
"""

try:
    from fastapi import Depends, FastAPI, HTTPException, status
    from pydantic import BaseModel
except ImportError:  # pragma: no cover
    FastAPI = None  # type: ignore

if FastAPI:

    app = FastAPI(title="Quick Revision API")

    class User(BaseModel):
        name: str
        age: int

    def auth_header(x_token: str | None = None):
        return x_token or "guest"

    @app.get("/")
    def home():
        return {"status": "ok"}

    @app.get("/users/{user_id}")
    def get_user(user_id: int):
        return {"user_id": user_id}

    @app.post("/users", status_code=status.HTTP_201_CREATED)
    def create_user(user: User):
        return user

    @app.get("/login")
    def login(username: str):
        if username != "admin":
            raise HTTPException(status_code=401, detail="unauthorized")
        return {"message": "ok"}

    @app.get("/depends")
    def with_dep(token: str = Depends(auth_header)):
        return {"token": token}

else:
    app = None


def run_revision() -> None:
    if app is None:
        print("Install fastapi: pip install fastapi uvicorn")
        print("Then: uvicorn quick_revision.day6_fastapi:app --reload")
        return
    print("FastAPI app ready. Routes:", [r.path for r in app.routes])
    print("Start: uvicorn day6_fastapi:app --reload  (from quick_revision/)")


if __name__ == "__main__":
    run_revision()