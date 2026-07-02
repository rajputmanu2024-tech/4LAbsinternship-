from fastapi import APIRouter, Body, Query,Path, HTTPException
from fastapi.responses import JSONResponse
from app.database  import load_data , save_data
from app.models import Student , StudentUpdate

router = APIRouter()


@router.get("/")
def home():
    return {"message" : "Welcome to the Student Management API"}

@router.get("/student")
def view_student():
    data=load_data()
    return data

@router.get("/student/{student_id}")
def student(student_id: int = Path(..., description="ID of the student",json_schema_extra={"example": "1"})):
    data = load_data()
    
    if student_id in data:
            return data[student_id]
    raise HTTPException(status_code=404, detail="Student not found")


@router.get("/sort")
def sort_student(sort_by:str=Query(...,description="see the student data in sorted order by age or name"),order:str=Query(default="asc",description="order of sorting can be 'asc' or 'desc', default is ascending")):

    if sort_by not in ["age", "name"] and order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort_by or order parameter.")
    data = load_data()
    return data


@router.post("/student")
def create_student(student: Student):
    data=load_data()
    if student.id in data:
        raise HTTPException(status_code=400, detail="Student with this ID already exists")
    data[student.id] = student.model_dump()

    save_data(data)

    return JSONResponse(content={"message": "Student created successfully ", "student": student.model_dump()}, status_code=201)


@router.put("/student/{student_id}")
def update_student(student_id:str,student:StudentUpdate):
    data=load_data()
    if student_id not in data:
        raise HTTPException(status_code=404, detail="Student not found")
    
    existing_student = data[student_id]
    updated_student = student.model_dump(exclude_unset=True)
   
    for key, value in updated_student.items():
        existing_student[key] = value
    
    existing_student['id'] = student_id  # Ensure the ID remains unchanged
    pydantic_student=Student(**existing_student)

    existing_student = pydantic_student.model_dump()
    data[student_id] = existing_student
    save_data(data)
    return {"message": "Student updated successfully", "student": existing_student}
    

@router.delete("/student/{student_id}")
def deletestudent(student_id:str=Path(...,description="ID of the student",json_schema_extra={"example":"1"})):
    data = load_data()
    if student_id not in data:
        raise HTTPException(status_code=404, detail="Student not found")
    deleted_student = data.pop(student_id)

    save_data(data)
    return {"message": "Student deleted successfully", "student": deleted_student}