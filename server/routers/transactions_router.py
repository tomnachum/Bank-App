from fastapi import APIRouter, status, HTTPException, Request
from db import MySqlManager, DB_NAME, extract_transaction
from db.exceptions import CategoryIdNotExist, UserIdNotExist, TransactionIdNotExist

router = APIRouter()
db_manager = MySqlManager(DB_NAME)


@router.get("/transactions", status_code=status.HTTP_200_OK)
def get_transactions():
    transactions = db_manager.get_all_transactions()
    return {"transactions": transactions}


@router.post("/transactions", status_code=status.HTTP_201_CREATED)
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


@router.delete("/transactions/{id}", status_code=status.HTTP_200_OK)
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
