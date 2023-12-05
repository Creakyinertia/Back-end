from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import apifile, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

desc = '''
1: Add student details to the database \n
2: Read a particular student's details \n
3: List out all the students \n
4: Update a student's details based on ID \n
5: Delete a student by ID \n
6: Get student details based on mobile and email \n
7: List all students by age \n
8: List all students by course taken \n
'''

app = FastAPI(title="Assessment-2", description=desc)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/student/")
async def get_student_based_on_id(student_name: str, db: Session = Depends(get_db)):
    return apifile.get_student_based_on_id(db, student_name)

@app.get("/students/")
async def get_all_students(db: Session = Depends(get_db)):
    return apifile.get_all_students(db)

@app.get("/student/mobile")
async def get_student_based_on_mobile_and_mail(phone: int, email: str, db: Session = Depends(get_db)):
    return apifile.get_student_based_on_mobile_and_mail(db,phone,email)

@app.get("/student/age")
async def get_student_based_on_age(age: int, db: Session = Depends(get_db)):
    return apifile.get_student_based_on_age(db,age)

@app.get("/student/course")
async def get_student_based_on_course(course: str, db: Session = Depends(get_db)):
    return apifile.get_student_based_on_course(db,course)

@app.post("/student/")
async def create_student_record(student: schemas.student, db: Session = Depends(get_db)):
    print(student)
    return apifile.post_item(db, student)

@app.put("/student/")
async def update_student_record(student_id:int, student: schemas.student, db: Session = Depends(get_db)):
    return apifile.update_student(db, student_id, student)

@app.delete("/student/{student_id}")
async def delete_student_record(student_id: int, db: Session = Depends(get_db)):
    return apifile.delete_item(db, student_id)

