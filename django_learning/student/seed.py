from faker import Faker
import random
from .models import *
fake = Faker()



def create_subject_marks(n):
    try:
        student_objects = Student.objects.all()
        for student in student_objects:
             subjects = Subject.objects.all()
             for subject in subjects:
                SubjectMarks.objects.create(student=student, subject=subject, marks=random.randint(0, 100))
    except Exception as e:
        print(f"Error occurred while creating subject marks: {e}")
      

def seed_db(n=100)-> None:


   # try:
        for _ in range(n):
            dep_object = Department.objects.all()
            random_index = random.randint(0, len(dep_object) - 1)
            student_department = dep_object[random_index]
            student_id = f'P{random.randint(100, 9999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 30)
            student_address = fake.address()


            student_id = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(
            student_id=student_id,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address,
            student_department=student_department
        )
    #except Exception as e:
       # print(f"Error occurred while seeding the database: {e}")