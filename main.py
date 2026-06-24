from fastapi import FastAPI
import uvicorn

from routes.employee_routes import router as employee_router
app = FastAPI()

@app.get("/")
def home():
    return {
        "msg": "Welcome to the Employee API",
        "status": "API is running"
    }

app.include_router(employee_router)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.3", port=8080)