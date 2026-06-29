from fastapi import FastAPI

app = FastAPI() #This is the object of the FastAPI class

@app.get("/") #This is a decorator that tells FastAPI that the function below is a route handler for the root endpoint
def hello():
    return {'message' : 'Hello World'}
   

@app.get('/about')
def about():
    return {'message' : 'This is a FastAPI application'}