from fastapi import APIRouter, status
from db import MySqlManager, DB_NAME

router = APIRouter()
db_manager = MySqlManager(DB_NAME)


@router.get("/categories/breakdown", status_code=status.HTTP_200_OK)
def get_categories_breakdown():
    breakdown = db_manager.get_breakdown_by_categories()
    return {"breakdown": breakdown}


@router.get("/categories", status_code=status.HTTP_200_OK)
def get_all_categories():
    categories = db_manager.get_all_categories()
    return {"categories": categories}
