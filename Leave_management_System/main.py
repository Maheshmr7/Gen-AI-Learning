from fastapi import FastAPI

app = FastAPI()

leaves = []

@app.get("/")
def home():
    return {
        "message": "Leave Management API Running"
    }

@app.post("/apply_leave")
def apply_leave(data: dict):

    leaves.append(data)

    return {
        "message": "Leave Applied Successfully"
    }

@app.get("/leaves")
def get_leaves():

    return leaves