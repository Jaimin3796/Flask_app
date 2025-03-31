from flask import request
from flask_restx import Namespace, Resource, fields
from services.student_service import StudentService

student_ns = Namespace("students", description="Student management operations")

student_model = student_ns.model("Student", {
    "student_id": fields.Integer(readonly=True, description="The unique identifier of a student"),
    "first_name": fields.String(required=True, description="First name of the student"),
    "last_name": fields.String(required=True, description="Last name of the student"),
    "dob": fields.String(required=True, description="Date of birth (YYYY-MM-DD)"),
    "amount_due": fields.Float(required=True, description="The fee amount pending for the student")
})

@student_ns.route("/")
class StudentList(Resource):
    @student_ns.doc("get_all_students")
    @student_ns.marshal_list_with(student_model)
    def get(self):
        """Get all students"""
        return StudentService.get_all_students()

    @student_ns.doc("create_student")
    @student_ns.expect(student_model)
    def post(self):
        """Create a new student"""
        data = request.get_json()
        student = StudentService.create_student(data)
        return {"message": "Student created", "student_id": student.student_id}, 201

@student_ns.route("/<int:student_id>")
class StudentResource(Resource):
    @student_ns.doc("get_student")
    @student_ns.marshal_with(student_model)
    def get(self, student_id):
        """Get a student by ID"""
        student = StudentService.get_student(student_id)
        if student:
            return student
        return {"message": "Student not found"}, 404

    @student_ns.doc("update_student")
    @student_ns.expect(student_model)
    def put(self, student_id):
        """Update student details"""
        data = request.get_json()
        student = StudentService.update_student(student_id, data)
        if student:
            return {"message": "Student updated"}
        return {"message": "Student not found"}, 404

    @student_ns.doc("delete_student")
    def delete(self, student_id):
        """Delete a student"""
        if StudentService.delete_student(student_id):
            return {"message": "Student deleted"}
        return {"message": "Student not found"}, 404
