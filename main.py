from fastapi import FastAPI      # Importing the fast API microservice.
import uvicorn        # Creating the connection for the server gateway interface. 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Chinedu"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
