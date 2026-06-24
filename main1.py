from fastapi import FastAPI
import uvicorn
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"Hello": "World"}
# create user API
users = [
    {"id":1, "name": "John"},
    {"id":2, "name": "Jane"},
    {"id":3, "name": "Jack"}
]
@app.get("/users")
def get_users():
    return users
 
@app.get("/users/{id}")
def get_user(id: int):
    for user in users:
        if user["id"] == id:
            return user
    return {"error": "User not found"}

get_users()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)