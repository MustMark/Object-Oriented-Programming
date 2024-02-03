def Check_Student(teacher_id):
    all_student = []
    for i in sub:
        for j in i.student_list:
            if teacher_id == i.teacher_list.teacher_id:
                all_student.append(j.student_name)
    return all_student
    
def Check_Subject(student_id):
    all_subject = []
    for i in sub:
        for j in i.student_list:
            if student_id in j.student_id:
                all_subject.append(i.subject_name)
    return all_subject

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

class Subject:
    def __init__(self, subject_id, subject_name, section, credit):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section
        self.credit = credit
        self.teacher_list = ""
        self.student_list = []

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

stu1 = Student("66011442", "Mark")
stu2 = Student("66010850", "Team")
stu3 = Student("66010786", "Earn")
stu4 = Student("66011490", "Third")
stu5 = Student("66010393", "Tham")
stu6 = Student("66010016", "Golf")

teach1 = Teacher("001", "KruLittle")
teach2 = Teacher("002", "KruBeam")
teach3 = Teacher("003", "KruLouis")
teach4 = Teacher("004", "KruOat")

sub = []
sub1 = Subject("01076105", "Object Oriented Programming", "116", 3)
sub2 = Subject("01076105", "Object Oriented Programming", "117", 3)
sub3 = Subject("01066000", "Calculus 1", "116", 3)
sub4 = Subject("01065300", "Charm School", "501", 3)
sub = [sub1,sub2,sub3,sub4]

sub1.teacher_list = teach1
sub2.teacher_list = teach2
sub3.teacher_list = teach3
sub4.teacher_list = teach4

sub1.student_list.append(stu1)
sub1.student_list.append(stu2)
sub1.student_list.append(stu3)
sub2.student_list.append(stu4)
sub2.student_list.append(stu5)
sub2.student_list.append(stu6)
sub3.student_list.append(stu1)
sub3.student_list.append(stu2)
sub3.student_list.append(stu3)
sub3.student_list.append(stu4)
sub4.student_list.append(stu1)
sub4.student_list.append(stu2)
sub4.student_list.append(stu5)
sub4.student_list.append(stu6)

print(Check_Student(input("Teacher_id : ")))

print(Check_Subject(input("Student_id : ")))