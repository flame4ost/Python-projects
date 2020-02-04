class University:
    def __init__(self, faculty, cathedra, staff, name="", age=0):
        self.name = name
        self.age = age
        self.fact = faculty
        self.cath = cathedra
        self.staff = staff

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_faculty(self, faculty):
        self.faculty = faculty

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_faculty(self):
        return self.faculty


un_size = 2
university = []
for i in range(un_size):
    un = University(input("\nchoose university: "), input("year: "), input(
        "faculty: "), input("cathedra: "), input("staff: "))


class Teacher:
    def __init__(self, salary, subject, d_year, age=0, full_name=""):
        self.age = age
        self.full_name = full_name
        self.subject = subject
        self.d_year = d_year
        self.salary = salary

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_age(self, age):
        self.age = age

    def set_faculty(self, salary):
        self.faculty = salary

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.age

    def get_subject(self):
        return self.subject


tr_size = 2
teacher = []
for i in range(tr_size):
    tr = teacher
    print("salary:")
    tr.salary = input()
    print("item:")
    tr.subject = input()
    print("birthyear: ")
    tr.d_year = input()


class Student:
    def __init__(self, full_name="", group_number=0, progress=[]):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def __repr__(self):
        return repr(("student: " + self.full_name + "  group: " + self.group_number))

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_group_number(self, group_number):
        self.group_number = group_number

    def set_progress(self, progress):
        self.progress = progress

    def get_full_name(self):
        return self.full_name

    def get_group_number(self):
        return self .group_number

    def get_progress(self):
        return self.progress


class caffedra(Teacher):
    def setCountTeacher(count):
        return sum(count)


class studRada(Student):
    def getCount(student):
        return sum(student)


st_size = 10
students = []
for i in range(st_size):
    st = Student()
    print("Enter full name: ")
    st.full_name = input()
    print("Enter group number: ")
    st.group_number = input()
    print("Enter five scores: ")
    st.progress = []
    for i in range(5):
        score = int(input())
        st.progress.append(score)
    students.append(st)
print("Sorted students:")
for st in students:
    print(st)

students = sorted(students, key=lambda student: student.full_name)
print("Sorted students:")
for st in students:
    print(st)

print("bad students:")
bad_studs = [stu for stu in students if any(
    x in stu.progress for x in [0, 1, 2])]


if len(bad_studs) > 0:
    for st in bad_studs:
        print(st)
else:
    print("no matches were found.")
