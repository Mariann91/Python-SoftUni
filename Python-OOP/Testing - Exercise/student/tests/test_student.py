from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student(
            name="Marian"
        )
        self.student_with_courses = Student(
            name="Monika",
            courses={"Math": "some note"}
        )

    def test_correct_initialization(self):
        self.assertEqual("Marian", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"Math": "some note"}, self.student_with_courses.courses)

    def test_correct_enroll_course_in_courses(self):
        self.student.courses["Math"] = []

        result = self.student.enroll(
            course_name="Math",
            notes=["note1", "note2", "note3"]
        )

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["note1", "note2", "note3"], self.student.courses["Math"])

    def test_enroll_add_course_notes_y_add_course_notes(self):
        result = self.student.enroll(
            course_name="Math",
            notes=["note1", "note2", "note3"],
            add_course_notes="Y"
        )

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Math": ["note1", "note2", "note3"]}, self.student.courses)

    def test_enroll_add_course_notes_empty_string_add_course_notes(self):
        result = self.student.enroll(
            course_name="Math",
            notes=["note1", "note2", "note3"],
            add_course_notes=""
        )

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Math": ["note1", "note2", "note3"]}, self.student.courses)

    def test_enroll_with_new_course_and_no_add_course_notes(self):
        result = self.student.enroll(
            course_name="Math",
            notes=["note1", "note2", "note3"],
            add_course_notes="N"
        )

        self.assertEqual("Course has been added.", result)
        self.assertEqual({"Math": []}, self.student.courses)

    def test_add_new_notes_in_existing_course(self):
        self.student.courses["Math"] = []
        result = self.student.add_notes("Math", "note1")
        # !
        self.assertEqual({"Math": ["note1"]}, self.student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_new_notes_with_not_existing_course_rises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Math", ["note1"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course(self):
        self.student.courses["Math"] = []
        result = self.student.leave_course("Math")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_not_existing_course_rises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Math")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    main()
