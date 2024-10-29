import unittest

from .student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        pass 
    def tearDown(self):
        pass


    def test_object_created_required_attributes(self):
        student = Student("Doe", "John", "Computer Science")
        assert student.last_name == "Doe"
        assert student.first_name == "John"
        assert student.major == "Computer Science"
        assert student.gpa == 0.0

    def test_object_created_all_attributes(self):
        student = Student("Doe", "John", "Computer Science", 3.5)
        assert student.last_name == "Doe"
        assert student.first_name == "John"
        assert student.major == "Computer Science"
        assert student.gpa == 3.5

    def test_student_str(self):
        student = Student("Doe", "John", "Computer Science", 3.5)
        assert str(student) == "Doe, John has major Computer Science with gpa: 3.5"

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = Student("", "John", "Computer Science")
    
    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = Student("Doe", "", "Computer Science")

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student = Student("Doe", "John", "", 2.0)


    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student = Student("Doe", "John", "Computer Science", 4.5)
        with self.assertRaises(ValueError):
            student = Student("Doe", "John", "Computer Science", -1.0)

if __name__ == '__main__':
    unittest.main()