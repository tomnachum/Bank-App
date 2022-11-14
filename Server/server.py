from fastapi import FastAPI, Request, Response, status
import uvicorn
import requests

app = FastAPI()


@app.get("/sanity")
def get_html():
    return {"Message": "Hello World"}


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
