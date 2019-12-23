class University:
    def __init__(self, name = "", age = 0, faculty, cathedra, staff):
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
un_size = 20
university = []
for i in range(un_size):
un = University(input("Университет: "), input("год: "), input("faculty: "), input("cathedra: "), input("staff: "))

class Teacher:
    def __init__(self, full_name = "", age = 0, salary, subject, d_year):
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
tr_size = 20
teacher = []
for i in range(tr_size):
tr = Teacher()
print("Зарплата:" )
tr.salary = input()
print("Предмет:")
tr.subject = input()
print("Год рождение: ")
tr.d_year = input()

class Student:
    def __init__(self,full_name = "", group_number = 0, progress = []):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress
    def __repr__(self):
     return repr(("Student: " + self.full_name + "  Group: " + self.group_number))
    def set_full_name(self, full_name):
         self.full_name = full_name
    def set_group_number(self, group_number):
         self.group_number = group_number
    def set_progress(self, progress):
         self.progress = progress
    def get_full_name(self):
         return self.full_name
    def get_group_number(self):
         return self.group_number
    def get_progress(self):
         return self.progress
 
st_size = 10
students = []
for i in range(st_size):
    st = Student()
    print("Enter full name: ")
    st.full_name = input()
    print("Enter group number: ")
    st.group_number= input()
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
bad_studs = [stu for stu in students if any (x in  stu.progress for x in [0, 1, 2])]
 
    
if len(bad_studs) > 0:
    for st in bad_studs:
        print(st)
else:
    print("no matches were found.")
