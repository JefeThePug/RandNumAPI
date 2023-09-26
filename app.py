from fastapi import FastAPI
import random
import sys


app = FastAPI()


@app.get("/api/v1/")
def index():
    outline = {
        "GET": {
            "/random": "random number between 0 and 1",
            "/randint/?a={n}": "random int between 0 and {n}",
            "/randint/?a={n}&b={j}": "random int between {n} and {j}"
        },
        "POST": {
            "TBD": "coming soon"
        }
    }
    return outline

@app.get("/api/v1/random")
def api_random():
    output = {"random number": random.random()}
    return output

@app.get("/api/v1/randint/")
def api_random(a: int, b: int = None):
    if b is None:
        a, b = 0, a
    output = {"random number": random.randint(a, b)}
    return output