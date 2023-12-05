from sqlalchemy.orm import Session
from . import models, schemas

def get_student_based_on_id(db: Session, student_name: str):
    comparison_name=student_name.upper()
    db_student = db.query(models.Students).filter(models.Students.name == comparison_name).first()
    return db_student

def get_all_students(db: Session):
    return db.query(models.Students).all()

def get_student_based_on_mobile_and_mail(db: Session, phone: int, email: str):
    db_item = db.query(models.Students).filter(models.Students.phone == phone, models.Students.email == email).first()
    return db_item

def get_student_based_on_age(db: Session, age: int):
    db_items = db.query(models.Students).filter(models.Students.age == age).all()
    return db_items

def get_student_based_on_course(db:Session,course_name:str):
    db_item = db.query(models.Students).filter(models.Students.course_name == course_name).all()
    return db_item

def post_item(db: Session, item: schemas.student):
    CAPSname=item.name.upper()
    new_item = models.Students(
        name=CAPSname,
        dob=item.dob,
        age=item.age,
        phone=item.phone,
        address=item.address,
        classname=item.classname,
        email=item.email,
        course_name=item.course_name
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_student(db: Session, student_id: int, item2: schemas.student):
    db_item = db.query(models.Students).filter(models.Students.id == student_id).first()
    if db_item:
        for attr, value in vars(item2).items():
            setattr(db_item, attr, value) if value is not None else None
        db.commit()
        db.refresh(db_item)
        return db_item
    return None

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Students).filter(models.Students.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item


