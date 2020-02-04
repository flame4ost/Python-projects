import sys


class University:
    def __init__(self, student_name=None, student_id=None, course_name=None, course_id=None):
        self._students = []
        self._courses = []
        self._enrolled = []
        self._student_name = student_name
        self._student_id = student_id
        self._course_name = course_name
        self._course_id = course_id

    @property
    def students(self):
        return self._students

    @property
    def courses(self):
        return self._courses

    @property
    def enrolled(self):
        return self._enrolled

    @property
    def student_name(self):
        return self._student_name

    @property
    def student_id(self):
        return self._student_id

    @property
    def course_name(self):
        return self._course_name

    @property
    def course_id(self):
        return self._course_id

    def create_course(self, course):
        self._courses.append(course)

    def list_courses(self):
        for i in self.courses:
            print(i)

    def enroll_student_in_course(self, student_name, student_id, course_name, course_id):
        self.enrolled.append(University(student_name, student_id, course_name, course_id))

    def enroll_student(self, student):
        self._students.append(student)

    def find_course(self, course_id):
        if course_id is 0:
            print(self.courses[0])
        for i in self.courses:
            if course_id == i.course_id:
                print(self.courses[course_id - 1])

    def find_student(self, student_id):
        if student_id is 0:
            print(self.students[0])
        for i in self.students:
            if student_id == i.student_id:
                print(self.students[student_id - 1])

    def list_enrolled_students(self, student_id):
        for i in self.enrolled:
            if student_id == i.student_id:
                print("Course #" + str(i.course_id) + ": " + i.course_name)

    def __str__(self):
        for i in self.enrolled:
            return "Course #" + str(i.course_id) + ": " + i.course_name


class Course:
    def __init__(self, course_name, course_id):
        self._course_name = course_name
        self._course_id = course_id

    @property
    def course_name(self):
        return self._course_name

    @property
    def course_id(self):
        return self._course_id

    def __str__(self):
        return "Course #" + str(self.course_id) + ": " + self.course_name


class Student:
    def __init__(self, student_name, student_id):
        self._student_name = student_name
        self._student_id = student_id

    @property
    def student_name(self):
        return self._student_name

    @property
    def student_id(self):
        return self._student_id

    def __str__(self):
        return self.student_name


def main():
    university = University()
    kevin = Student("Kevin", 1)
    cedric = Student("Cedric", 2)

    engl_101 = Course("English 101", 1)
    math_248 = Course("Math 248", 2)
    cs_201 = Course("Computer Science 201", 3)
    cs_420 = Course("Computer Science 420", 4)
    rels_345 = Course("Religious Studies 345", 5)
    cs_462 = Course("Senior Design II", 6)

    university.create_course(engl_101)
    university.create_course(math_248)
    university.create_course(cs_201)
    university.create_course(cs_420)
    university.create_course(rels_345)
    university.create_course(cs_462)

    university.enroll_student(kevin)
    university.enroll_student(cedric)

    print(kevin.student_name + ", Student ID #" + str(kevin.student_id) + " is enrolled in:")
    university.enroll_student_in_course(kevin.student_name, kevin.student_id, cs_420.course_name, cs_420.course_id)
    university.enroll_student_in_course(kevin.student_name, kevin.student_id, rels_345.course_name, rels_345.course_id)
    university.enroll_student_in_course(kevin.student_name, kevin.student_id, cs_462.course_name, cs_462.course_id)
    university.list_enrolled_students(1)

    print("\n" + cedric.student_name + ", Student ID #" + str(cedric.student_id) + " is enrolled in:")
    university.enroll_student_in_course(cedric.student_name, cedric.student_id, cs_420.course_name, cs_420.course_id)
    university.enroll_student_in_course(cedric.student_name, cedric.student_id, cs_462.course_name, cs_462.course_id)
    university.list_enrolled_students(2)


if __name__ == '__main__':
    sys.exit(main())
