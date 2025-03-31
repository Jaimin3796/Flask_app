from models.student import Student
from repositories.student_repository import StudentRepository

class StudentService:
    @staticmethod
    def create_student(data):
        new_student = Student(**data)
        return StudentRepository.create_student(new_student)

    @staticmethod
    def get_student(student_id):
        return StudentRepository.get_student_by_id(student_id)

    @staticmethod
    def get_all_students():
        return StudentRepository.get_all_students()

    @staticmethod
    def update_student(student_id, data):
        student = StudentRepository.get_student_by_id(student_id)
        if student:
            for key, value in data.items():
                setattr(student, key, value)
            return StudentRepository.update_student(student)
        return None

    @staticmethod
    def delete_student(student_id):
        student = StudentRepository.get_student_by_id(student_id)
        if student:
            StudentRepository.delete_student(student)
            return True
        return False
