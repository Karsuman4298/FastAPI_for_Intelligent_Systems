from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Patiant management  system API"}

@app.get("/about")
def about():
    return {"message": "functional API to manage patient records"}


def load_data():
    with open("patient.json", "r") as f:
       data=json.load(f)

    return data   


@app.get("/view")
def view():
    data=load_data()
    return data    