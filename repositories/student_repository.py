from extensions import db
from models.student import Student

class StudentRepository:
    @staticmethod
    def create_student(student):
        db.session.add(student)
        return student

    @staticmethod
    def get_student_by_id(student_id):
        return Student.query.get(student_id)

    @staticmethod
    def get_all_students():
        return Student.query.all()

    @staticmethod
    def update_student(student):
        db.session.commit()
        return student

    @staticmethod
    def delete_student(student):
        db.session.delete(student)
        db.session.commit()
