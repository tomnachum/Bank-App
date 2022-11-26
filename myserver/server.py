import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import transactions_router, categories_router, users_router

CLIENT_DOMAIN = "http://localhost:3000"

app = FastAPI()

app.include_router(transactions_router.router)
app.include_router(categories_router.router)
app.include_router(users_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CLIENT_DOMAIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
