import uvicorn
import requests
from fastapi import FastAPI, Request, Response, status, HTTPException
from fastapi.responses import JSONResponse
from db import MySqlManager, DB_NAME, extract_transaction, Transaction
from db.exceptions import CategoryIdNotExist, UserIdNotExist

app = FastAPI()
db_manager = MySqlManager(DB_NAME)


@app.get("/transactions", status_code=status.HTTP_200_OK)
def get_transactions():
    transactions = db_manager.get_all_transactions()
    return {"transactions": transactions}


@app.post("/transactions", status_code=status.HTTP_200_OK)
async def add_transaction(request: Request):
    transaction_data = await request.json()
    transaction = extract_transaction(transaction_data)
    try:
        db_manager.add_transaction(transaction)
        return {"Message": "Transaction added successfully"}
    except CategoryIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except UserIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )


# @app.get("/check")
# def get_players():
#     return {"check": "OK"}

# ----------------------------- a request with a body
# @app.put("/endpoint")
# async def add_player(request: Request):
#     body = await request.json()

# ----------------------------- external api call
# def external_api_call():
#     pokemon_response = requests.get(
#         f"https://pokeapi.co/api/v2/pokemon/{p_name}"
#     ).json()

# ----------------------------- status code
# @app.put("/get-or-create-task/{task_id}", status_code=status.HTTP_200_OK)
# def get_or_create_task(task_id: str, response: Response):
#     if task_id not in tasks:
#         tasks[task_id] = "This didn't exist before"
#         response.status_code = status.HTTP_201_CREATED
#     return tasks[task_id]

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
