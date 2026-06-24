from fastapi import FastAPI
import uvicorn
app=FastAPI()
@app.get("/")
def get_root():
    return {"message":"Hello World"}
users=[{"name":"John","age":30},
       {"name":"Jane","age":25},
       {"name":"Doe","age":40}]
@app.get("/users")
def get_users():
    return users

@app.post("/users")
def add_user(user:dict):
    users.append(user)
    return {"message":"User added successfully"}

@app.put("/users/{user_id}")
def update_user(user_id:int, user:dict):
    if user_id<0 or user_id>=len(users):
        return {"message":"User not found"}
    users[user_id]=user
    return {"message":"User updated successfully"}
    raise NotImplementedError("Update user functionality not implemented yet")

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    if user_id<0 or user_id>=len(users):
        return {"message":"User not found"}
    users.pop(user_id)
    return {"message":"User deleted successfully"}
    raise NotImplementedError("Delete user functionality not implemented yet")

