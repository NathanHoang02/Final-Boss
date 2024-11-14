#student_crud 
class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentRegistrationSystem:
    def __init__(self):
        self.students = {}

    # CREATE
    def create_student(self, student_id, name, age, major):
        if student_id in self.students:
            print("Student with this ID already exists.")
            return False
        else:
            self.students[student_id] = Student(student_id, name, age, major)
            print("Student created successfully.")
            return True

    # READ
    def read_student(self, student_id):
        if student_id in self.students:
            print(str(self.students[student_id]) + "\n")
            return student_id
        else:
            print("Student not found.")

    def read_all_students(self):
        if not self.students:
            print("No students registered.")
            return []
        else:
            for student in self.students.values():
                print(str(student))
            return self.students.values()

    # UPDATE
    def update_student(self, student_id, name=None, age=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
            print("Student updated successfully.")
            return True
        else:
            print("Student not found.")
            return False

    # DELETE
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
            return True
        else:
            print("Student not found.")
            return False

import unittest
from Test import StudentRegistrationSystem

class TestRegistrationSystem(unittest.TestCase):
    def setUp(self):
        self.registration = StudentRegistrationSystem()
        # Add initial student for test setup.
        self.registration.create_student(student_id=1, name='Mike', age=8, major='Roar Management')

    def test_create_student_success(self):
        # Testing creating a new student successfully
        result = self.registration.create_student(student_id=2, name='Jane', age=22, major='Philosophy')
        self.assertTrue(result)
        self.assertIn(2, self.registration.students)
        self.assertEqual(self.registration.students[2].name, 'Jane')
        self.assertEqual(self.registration.students[2].age, 22)
        self.assertEqual(self.registration.students[2].major, 'Philosophy')

    def test_create_student_duplicate_id(self):
        # Testing creation of a student with a duplicate ID
        result = self.registration.create_student(student_id=1, name='Duplicate', age=30, major='Physics')
        self.assertFalse(result)
        self.assertEqual(self.registration.students[1].name, 'Mike')  # Original student remains

    def test_read_student_success(self):
        # Testing reading an existing student
        result = self.registration.read_student(student_id=1)
        self.assertEqual(result, 1)

    def test_read_student_not_found(self):
        # Testing reading a non-existent student
        result = self.registration.read_student(student_id=99)
        self.assertIsNone(result)

    def test_read_all_students(self):
        # Testing reading all students (should contain one initially)
        result = self.registration.read_all_students()
        self.assertEqual(len(result), 1)

    def test_update_student_success(self):
        # Testing updating an existing student
        result = self.registration.update_student(student_id=1, name='Michael', age=9, major='Roar Advanced')
        self.assertTrue(result)
        self.assertEqual(self.registration.students[1].name, 'Michael')
        self.assertEqual(self.registration.students[1].age, 9)
        self.assertEqual(self.registration.students[1].major, 'Roar Advanced')

    def test_update_student_not_found(self):
        # Testing updating a non-existent student
        result = self.registration.update_student(student_id=99, name='Non-existent')
        self.assertFalse(result)

    def test_update_student_partial_data(self):
        # Testing partial update of an existing student
        result = self.registration.update_student(student_id=1, major='Jungle Studies')
        self.assertTrue(result)
        self.assertEqual(self.registration.students[1].major, 'Jungle Studies')
        self.assertEqual(self.registration.students[1].name, 'Mike')  # Name should remain unchanged

    def test_delete_student_success(self):
        # Testing deletion of an existing student
        result = self.registration.delete_student(student_id=1)
        self.assertTrue(result)
        self.assertNotIn(1, self.registration.students)

    def test_delete_student_not_found(self):
        # Testing deletion of a non-existent student
        result = self.registration.delete_student(student_id=99)
        self.assertFalse(result)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRegistrationSystem))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
