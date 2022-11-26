from fastapi import APIRouter, status, HTTPException
from db import MySqlManager, DB_NAME
from db.exceptions import UserIdNotExist

router = APIRouter()
db_manager = MySqlManager(DB_NAME)


@router.get("/users/{id}/balance", status_code=status.HTTP_200_OK)
def get_user_balance(id):
    try:
        balance = db_manager.get_balance(id)
        return {"balance": balance}
    except UserIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )
