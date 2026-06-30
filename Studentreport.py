from fastapi import FastAPI,HTTPException,Query

app=FastAPI()

@app.get("/")
def home():
    return {"message" : "Welcome to the Student Report API"}

@app.get("/student/{name}")
def student(name:str):
    return {"name": name,
            "Grade": "A",}



@app.get("/student/{name}/score")
def marks(name:str, score:int=Query(..., ge=0, le=100, description="The score of the student")):
    #ge for greater than or equal to, le for less than or equal to
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    return {"name": name, "score": score, "grade": grade}