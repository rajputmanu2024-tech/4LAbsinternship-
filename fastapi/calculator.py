from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
    return {"message":"Calculator API"}

@app.get('/add')
def add(a:float,b:float):
    return {'result': a+b}

@app.get('/subtract')
def subtract(a:float , b: float):
    return {"result":a-b}

@app.get('/multiply')
def multiply(a:float,b:float):
    return {"result": a*b}

@app.get('/divide')
def divide(a:float,b:float):
    if b==0:
        return {"error":"denominator cannot be zero"}
    return {"result": a//b}

@app.get('/modulus')
def modulus(a:float,b:float):
    if b==0:
        return {"error":"denominator cannot be zero"}
    return {"result": a%b}

@app.get('/power')
def power(a:float,b:float):
    return {"result": a**b} 
    

@app.get('/calculate')
def calculate(a:float,b:float):
    return {"addition": a+b, 
            "subtraction": a-b,
            "multiplication": a*b,
            "division": a/b if b!=0 else "undefined",
            "modulus": a%b if b!=0 else "undefined",
            "power": a**b}