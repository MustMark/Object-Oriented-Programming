def Show_Mentor(id):
    all_mentor = []
    if int(id)/1000000 == 63:
        return "No Mentor"
    for i in stu:
        if id == i.student_id and i.student_mentor != None:
            all_mentor.append(i.student_mentor.student_id + " " +i.student_mentor.student_name)
            id = i.student_mentor.student_id
    return all_mentor
    
def Check_Mentor(stu_x,stu_y):
    if int(stu_x)/1000000 == int(stu_y)/1000000:
        return False
    elif int(stu_x)/1000000 < int(stu_y)/1000000:
        stu_x,stu_y = stu_y,stu_x
    mentor = Show_Mentor(str(stu_x))
    for i in stu:
        if stu_y == i.student_id:
            stu_y = stu_y + " " + i.student_name
    if stu_y in mentor:
        return True
    else:
        return False

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_mentor = None
    def add_mentor(self, older):
        self.student_mentor = older

stu = []
stu1 = Student("66011442", "Mark")
stu2 = Student("65010850", "Team")
stu3 = Student("64010786", "Earn")
stu4 = Student("63011490", "Third")
stu5 = Student("66010393", "Tham")
stu6 = Student("65010016", "Golf")
stu7 = Student("64011500", "Pizza")
stu8 = Student("63010221", "Shabu")
stu = [stu1,stu2,stu3,stu4,stu5,stu6,stu7,stu8]

for i in range(len(stu) - 1):
    if i != 3:
        stu[i].add_mentor(stu[i+1])

print(Show_Mentor(input("Student id : ")))

stu_x = input("Student x id : ")
stu_y = input("Student y id : ")
print(Check_Mentor(stu_x,stu_y))