from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import random

app = FastAPI()

# This middleware is required in order to accept requests from other domains such as a React app running on 'localhost:3000'
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def root():
    return({ "message": "hello world" })

@app.get("/flip-coin")
def flip_coin():
    flip = random.random()
    if (flip >= 0.5): 
        return({"value": "heads"})
    else:
        return({"value": "tails"})

@app.get("/flip-coins")
def flip_coins(times: int = 10):
    if (times > 0):
        head_count = 0
        tail_count = 0
        for i in range(times):
            flip = random.random()
            if (flip >= 0.5):
                head_count += 1
            else:
                tail_count += 1
        return({"heads": head_count, "tails": tail_count})
    else:
        return({"message": "are you stupid"})

@app.get("/guess-coin")
def guess_coin(guess: str):
    if (guess == "heads" or guess == "tails"):
        flip = random.random()
        if (flip >= 0.5):
            if (guess == "heads"):
                return({"message": "congrats you won"})
            else:
                return({"message": "gg go next"})
        else:
            if (guess == "tails"):
                return({"message": "congrats you won"})
            else:
                return({"message": "gg go next"})
    else:
        return({"message": "are you fr"})

                

if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, reload=True)

