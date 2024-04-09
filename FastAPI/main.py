from fastapi import FastAPI

app = FastAPI()

# This a path operation decorator 
# @app.post()
# @app.put()
# @app.delete()

@app.get("/intro")
async def root():
    return {"message":"Hello there budd! How you doin!?"}

@app.get("/infos")
def info():
    return {"Names":['Lisa', 'Jason', 'Brad', 'Riley', 'Vaas'],
            "Age":[26,28,31,23,33]}

@app.post("/fetch")
def fetcher():
    return {"Using POST method"}