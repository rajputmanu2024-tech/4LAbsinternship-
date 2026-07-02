from pydantic import BaseModel,Field,EmailStr
from typing import Optional,Annotated,Literal



class Address(BaseModel):
    city: Annotated[str, Field(...,min_length=1, max_length=50, description="City of the student")]
    state:Annotated[str,Field(...,descrtiption="State of the student",json_schema_extra={"example":"Punjab"})]
    pincode: Annotated[str, Field(..., description="Pincode of the student")]

class Student(BaseModel):
    id: Annotated[str, Field(...,description="ID of the student",json_schema_extra={"example":"1"})]
    name: Annotated[str, Field(...,min_length=1, max_length=50, description="Name of the student")]
    age:Annotated[Optional[int], Field(default=None, ge=4, le=25, description="Age of the student")]
    gender: Annotated[Literal["Male","Female","Other"], Field(..., description="Gender of the student")]
    course_or_class: Annotated[str, Field(...,min_length=1, max_length=50, description="Course or class of the student")]
    branch: Annotated[str, Field(...,min_length=1, max_length=50, description="Branch of the student")]
    year_of_study: Annotated[Optional[int], Field(default=None, ge=1, le=5, description="Year of study of the student")]
    email: Annotated[EmailStr, Field(default=None, description="Email of the student")]
    phone_number: Annotated[Optional[str], Field(default=None, max_length=10, description="Phone number of the student")]
    address: Annotated[Address, Field(default=None, description="Address of the student")]


class StudentUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None, min_length=1, max_length=50, description="Name of the student")]
    age:Annotated[Optional[int], Field(default=None, ge=4, le=25, description="Age of the student")]
    gender: Annotated[Optional[Literal["Male","Female","Other"]], Field(default=None, description="Gender of the student")]
    course_or_class: Annotated[Optional[str], Field(default=None, min_length=1, max_length=50, description="Course or class of the student")]
    branch: Annotated[Optional[str], Field(default=None, min_length=1, max_length=50, description="Branch of the student")]
    year_of_study: Annotated[Optional[int], Field(default=None, ge=1, le=5, description="Year of study of the student")]
    email: Annotated[Optional[EmailStr], Field(default=None, description="Email of the student")]
    phone_number: Annotated[Optional[str], Field(default=None, max_length=10, description="Phone number of the student")]
    address: Annotated[Optional[Address], Field(default=None, description="Address of the student")]

