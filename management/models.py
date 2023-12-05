from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Students(Base):
    __tablename__ = 'Students'
    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    name = Column(String(50))
    dob = Column(String(50))
    age = Column(Integer)
    phone = Column(Integer)
    address = Column(String(100)) 
    classname = Column(String(50)) 
    email = Column(String(50))
    course_name = Column(String(50))

    courses = relationship("Courses", back_populates="student")

class Courses(Base):
    __tablename__ = 'Courses'
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(50), nullable=False)  
    description = Column(String(100)) 
    student_id = Column(Integer, ForeignKey('Students.id')) 
    student = relationship("Students", back_populates="courses")
