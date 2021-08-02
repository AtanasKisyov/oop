from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student("Pesho")
        self.student_with_courses = Student("Smart Pesho", courses={"Python": ["Y"]})

    def test_correct_initialization(self):
        self.assertEqual("Pesho", self.student.name)
        self.assertEqual({},  self.student.courses)
        self.assertEqual("Smart Pesho", self.student_with_courses.name)
        self.assertEqual({"Python": ["Y"]}, self.student_with_courses.courses)

    def test_enroll_already_added_course(self):
        expected = "Course already added. Notes have been updated."
        result = self.student_with_courses.enroll("Python", "S")
        self.assertEqual({"Python": ["Y", "S"]}, self.student_with_courses.courses)
        self.assertEqual(expected, result)

    def test_enroll_Y_notes(self):
        expected = "Course and course notes have been added."
        result = self.student_with_courses.enroll("Java", "S", add_course_notes="Y")
        self.assertEqual(expected, result)
        self.assertEqual({"Java": "S", "Python": ["Y"]}, self.student_with_courses.courses)

    def test_enroll_empty_course_notes(self):
        expected = "Course and course notes have been added."
        result = self.student_with_courses.enroll("Java", "S", add_course_notes="")
        self.assertEqual(expected, result)
        self.assertEqual({"Java": "S", "Python": ["Y"]}, self.student_with_courses.courses)

    def test_enroll_added_course(self):
        expected = "Course has been added."
        result = self.student_with_courses.enroll("Java", "S", "Sekish")
        self.assertEqual(expected, result)
        self.assertEqual({"Java": [], "Python": ["Y"]}, self.student_with_courses.courses)

    def test_add_notes_raises(self):
        with self.assertRaises(Exception) as e:
            self.student.add_notes("Python", "Y")
        self.assertEqual("Cannot add notes. Course not found.", str(e.exception))

    def test_add_notes(self):
        self.student_with_courses.add_notes("Python", "S")
        self.assertEqual({"Python": ["Y", "S"]}, self.student_with_courses.courses)

    def test_leave_course_raises(self):
        with self.assertRaises(Exception) as e:
            self.student.leave_course("Python")
        self.assertEqual("Cannot remove course. Course not found.", str(e.exception))

    def test_leave_course(self):
        expected = "Course has been removed"
        result = self.student_with_courses.leave_course("Python")
        self.assertEqual(expected, result)
        self.assertEqual({}, self.student_with_courses.courses)


if __name__ == "__main__":
    main()
