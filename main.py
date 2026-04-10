from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hii"}

@app.get("/about")
def about():
    return {"message": "This is the About page"}

@app.get("/kill")
def kill():
    return {"message": "This is the kill page"}    