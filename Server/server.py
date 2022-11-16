import uvicorn
import requests
from fastapi import FastAPI, Request, Response, status, HTTPException
from fastapi.responses import JSONResponse
from db import MySqlManager, DB_NAME, extract_transaction, Transaction
from db.exceptions import CategoryIdNotExist, UserIdNotExist, TransactionIdNotExist

app = FastAPI()
db_manager = MySqlManager(DB_NAME)


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
        db_manager.delete_transaction(id)
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


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
