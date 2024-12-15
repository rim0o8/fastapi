from middleware.cors import add_cors_middleware
from middleware.router import add_router

from fastapi import FastAPI

app = FastAPI()
app = add_cors_middleware(app)
app = add_router(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, log_level="info")
