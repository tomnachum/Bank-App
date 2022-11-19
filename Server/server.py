import uvicorn
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import MySqlManager, DB_NAME, CLIENT_DOMAIN, extract_transaction
from db.exceptions import CategoryIdNotExist, UserIdNotExist, TransactionIdNotExist

app = FastAPI()
db_manager = MySqlManager(DB_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CLIENT_DOMAIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/transactions", status_code=status.HTTP_200_OK)
def get_transactions():
    transactions = db_manager.get_all_transactions()
    return {"transactions": transactions}


@app.post("/transactions", status_code=status.HTTP_201_CREATED)
async def add_transaction(request: Request):
    transaction_data = await request.json()
    transaction = extract_transaction(transaction_data)
    try:
        db_manager.add_transaction(transaction)
        return {"Message": "Transaction added successfully"}
    except CategoryIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )
    except UserIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )


@app.delete("/transactions/{id}", status_code=status.HTTP_200_OK)
def delete_transaction(id: int):
    try:
        transaction = db_manager.get_transaction_by_id(id)
        db_manager.delete_transaction(transaction)
        return {"Message": "Transaction deleted successfully"}
    except TransactionIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )


@app.get("/categories/breakdown", status_code=status.HTTP_200_OK)
def get_categories_breakdown():
    breakdown = db_manager.get_breakdown_by_categories()
    return {"breakdown": breakdown}


@app.get("/categories", status_code=status.HTTP_200_OK)
def get_all_categories():
    categories = db_manager.get_all_categories()
    return {"categories": categories}


@app.get("/users/{id}/balance", status_code=status.HTTP_200_OK)
def get_user_balance(id):
    try:
        balance = db_manager.get_balance(id)
        return {"balance": balance}
    except UserIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
