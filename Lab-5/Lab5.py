class Student:
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name
    def get_student_id(self):
        return self.__student_id
    def get_student_name(self):
        return self.__student_name
        
class Subject:
    def __init__(self, subject_id, subject_name, credit):
        self.__subject_id = subject_id
        self.__subject_name = subject_name
        self.__credit = credit
        self.__teacher = None
    def assign_teacher(self, teacher):
        self.__teacher = teacher
    def get_teacher_name(self):
        return self.__teacher
    def get_subject_name(self):
        return self.__subject_name
    def get_subject_id(self):
        return self.__subject_id
    def get_credit(self):
        return self.__credit

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.__teacher_id = teacher_id
        self.__teacher_name = teacher_name
    def get_name(self):
        return self.__teacher_name

class Enrollment:
    def __init__(self, student, subject):
        self.__student = student
        self.__subject = subject
        self.__grade = ""

    def get_student(self):
        return self.__student
    
    def get_subject(self):
        return self.__subject
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self,grade):
        self.__grade = grade

def search_subject_by_id(subject_id):
    for i in subject_list:
        if subject_id == i.get_subject_id():
            return i
def search_student_by_id(student_id):
    for i in student_list:
        if student_id == i.get_student_id():
            return i
def enroll_to_subject(student, subject):
    if student not in student_list or subject not in subject_list:
        return "Error"
    for i in enrollment_list:
        if student == i.get_student() and subject == i.get_subject():
            return "Already Enrolled"
    enrollment_list.append(Enrollment(student, subject))
    return "Done"

def drop_from_subject(student, subject):
    if student not in student_list or subject not in subject_list:
        return "Error"
    for i in enrollment_list:
        if student == i.get_student() and subject == i.get_subject():
            enrollment_list.remove(i)
            return "Done"
    return "Not Found"

def search_enrollment_subject_student(subject, student):
    if student not in student_list or subject not in subject_list:
        return "Error"
    for i in enrollment_list:
        if student == i.get_student() and subject == i.get_subject():
            return i
    return "Not Found"
    
def search_student_enroll_in_subject(subject):
    all_student = []
    if subject not in subject_list:
        return "Error"
    for i in enrollment_list:
        if subject == i.get_subject():
            all_student.append(i.get_student())
    if all_student == []:
        return "Not Found"
    else:
        return all_student
    
def search_subject_that_student_enrolled(student):
    all_subject = []
    if student not in student_list:
        return "Error"
    for i in enrollment_list:
        if student == i.get_student():
            all_subject.append(i.get_subject())
    if all_subject == []:
        return "Not Found"
    else:
        return all_subject
    
def get_teacher_teach(subject):
    return subject.get_teacher_name()

def get_no_of_student_enrolled(subject):
    count = 0
    if subject not in subject_list:
        return "Not Found"
    for i in enrollment_list:
        if subject == i.get_subject():
            count += 1
    return count

def assign_grade(student, subject, grade):
    i = search_enrollment_subject_student(subject, student)
    if isinstance(i, Enrollment):
        if i.get_grade() == "":
            i.set_grade(grade)
            return "Done"
        else:
            return "Error"
    else:
        return "Not Found"
    
def get_student_record(student):
    record = {}
    for i in enrollment_list:
        if student == i.get_student() and i.get_grade() != "":
            record[i.get_subject().get_subject_id()] = [i.get_subject().get_subject_name(),i.get_grade()]
    return record

def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping.get(grade, 0)

def get_student_GPS(student):
    record = get_student_record(student)
    sum = 0
    credit = 0
    for i in enrollment_list:
        if student == i.get_student():
            sum += grade_to_count(i.get_grade())*i.get_subject().get_credit()
            credit += i.get_subject().get_credit()
    return sum/credit

def list_student_enrolled_in_subject(subject_id):
    subject = search_subject_by_id(subject_id)
    if subject is None:
        return "Subject not found"
    student_dict = {}
    for i in search_student_enroll_in_subject(subject):
        student_dict[i.get_student_id()] = i.get_student_name()
    return student_dict

def list_subject_enrolled_by_student(student_id):
    student = search_student_by_id(student_id)
    if student is None:
        return "Student not found"
    subject_dict = {}
    for i in search_subject_that_student_enrolled(student):
        subject_dict[i.get_subject_id()] = i.get_subject_name()
    return subject_dict

def create_instance():
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 3))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 4))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])

def register():
    enroll_to_subject(student_list[0], subject_list[0])  # 001 -> CS101
    enroll_to_subject(student_list[0], subject_list[1])  # 001 -> CS102
    enroll_to_subject(student_list[0], subject_list[2])  # 001 -> CS103
    enroll_to_subject(student_list[1], subject_list[0])  # 002 -> CS101
    enroll_to_subject(student_list[1], subject_list[1])  # 002 -> CS102
    enroll_to_subject(student_list[1], subject_list[2])  # 002 -> CS103
    enroll_to_subject(student_list[2], subject_list[0])  # 003 -> CS101
    enroll_to_subject(student_list[2], subject_list[1])  # 003 -> CS102
    enroll_to_subject(student_list[2], subject_list[2])  # 003 -> CS103
    enroll_to_subject(student_list[3], subject_list[0])  # 004 -> CS101
    enroll_to_subject(student_list[3], subject_list[1])  # 004 -> CS102
    enroll_to_subject(student_list[4], subject_list[0])  # 005 -> CS101
    enroll_to_subject(student_list[4], subject_list[2])  # 005 -> CS103
    enroll_to_subject(student_list[5], subject_list[1])  # 006 -> CS102
    enroll_to_subject(student_list[5], subject_list[2])  # 006 -> CS103
    enroll_to_subject(student_list[6], subject_list[0])  # 007 -> CS101
    enroll_to_subject(student_list[7], subject_list[1])  # 008 -> CS102
    enroll_to_subject(student_list[8], subject_list[2])  # 009 -> CS103

student_list = []
subject_list = []
teacher_list = []
enrollment_list = []

create_instance()
register()

### Test Case #1 : test enroll_to_subject complete ###
student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print(student_enroll)
print("")

### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
print("Answer : Error")
print(enroll_to_subject('66010001','CS101'))
print("")

### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
print("Answer : Already Enrolled")
print(enroll_to_subject(student_list[0], subject_list[0]))
print("")

### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
print("Answer : Error")
print(drop_from_subject('66010001', 'CS101'))
print("")

### Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
print("Answer : Not Found")
print(drop_from_subject(student_list[8], subject_list[0]))
print("")

### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
drop_from_subject(student_list[0], subject_list[0])
print(list_student_enrolled_in_subject(subject_list[0].get_subject_id()))
print("")

### Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enroll_in_subject(subject_list[0])
print([i.get_student_id() for i in lst])
print("")

### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
print("Answer : 5")
print(get_no_of_student_enrolled(subject_list[0]))
print("")

### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
print("Answer : ['CS102','CS103']")
lst = search_subject_that_student_enrolled(student_list[0])
print([i.get_subject_id() for i in lst])
print("")

### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
print("Answer : Mr. Welsh")
print(get_teacher_teach(subject_list[0]).get_name())
print("")

### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
print("Answer : CS101 66010002")
enroll = search_enrollment_subject_student(subject_list[0],student_list[1])
print(enroll.get_subject().get_subject_id(),enroll.get_student().get_student_id())
print("")

### Test case #12 : assign_grade
print("Test case #12 assign_grade")
print("Answer : Done")
assign_grade(student_list[1],subject_list[0],'A')
assign_grade(student_list[1],subject_list[1],'B')
print(assign_grade(student_list[1],subject_list[2],'C'))
print("")

### Test case #13 : get_student_record
print("Test case #13 get_student_record")
print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print(get_student_record(student_list[1]))
print("")

### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
print("Answer : 2.9")
print(get_student_GPS(student_list[1]))