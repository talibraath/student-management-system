import os
import datetime
import json

courses = {
    "CS1001": "Programming Fundamentals",
    "CS1002": "OOP",
    "CS1003": "Data Structures"
}

attendance = {
    #"21F-9070": {"CS1001": [15]}
}

Grades = {
    # rollno: {course_id: grade}
}
class Student:
    
    def __init__(self, name, rollno, age, gender):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.gender = gender
        self.registered_courses = set()
    

    def get_dict(self):
        d = {
        "name": self.name,
        "rollno": self.rollno,
        "age": self.age,
        "gender": self.gender,
        "registered_courses": list(self.registered_courses)
        }
        return d
class CustomList:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        for s in self.students:
            if student.rollno in s.rollno:
                print(f"This {student.rollno} rollno already exist")
                return
        self.students.append(student)
        return

            
    def view_all_students(self):
       return self.students
        
    # def get_student(self,rollno):
    #    data = [student for student in self.students]
    #    if(data):
    #        return data[0]
    #    print("This student does not exist.")
    #    return "None"
    def get_student(self, rollno):
     for student in self.students:
        if student.rollno == rollno:
            return student
     print("This student does not exist.")
     return "None"
    
    def get_dict(self):
        return [student.get_dict() for student in self.students]



def enroll_student(*,student,course_id):
    if course_id in courses:
        if(course_id in student.registered_courses):
            print(f"Already Registered to {course_id}")
            return
        student.registered_courses.add(course_id)
        print(f"{student.rollno} has been registered to {course_id}\n")
    else:
        print("Courses does not exist in database")


def add_course(*,course_id,course_name):
    global courses
    if(course_id in courses):
        print("Course Already Exist")
        return
    courses[course_id] = course_name
    print("Course has been added")

def mark_attendance(stud_data):
    check = True
    course_id = input("Enter Course ID: ")
    today_date = datetime.datetime.now().date()
    if course_id in courses:
        while(check):
          student_rollno = input("Enter Rollno: or 0 to exit: ")
          if(student_rollno == "0"):
              print("Exiting")
              return
          else:
              s = stud_data.get_student(student_rollno)
             
              if(s != 'None'):
                if(course_id in s.registered_courses):
                    if student_rollno not in attendance:
                        attendance[student_rollno] = {}
                    if course_id not in attendance[student_rollno]:
                        attendance[student_rollno][course_id] = []
                    attendance[student_rollno][course_id].append(str(today_date))

                else:
                  print(f"Student not registered to course {course_id}")
    
    else:
        print(f"{course_id} course does not exist")





def add_grades(students):
    global courses
    
    check =True
    while(check):
        course_id = input("Enter Course ID: ")
        if course_id not in courses:
            print("Invalid Courses")
        else:
            check = False

    while (True):
        rollno = input("Enter Rollno: or 0 to exit: ")
        if(rollno == "0"):
            return
        student = students.get_student(rollno)
        if(student =="None"):
            continue
        if(course_id in student.registered_courses):
            grade = input("Enter Grade: or 0 to exit: ")
            if(grade == "0"):
                return
            if rollno not in Grades:
                Grades[rollno] = {}
            Grades[rollno][course_id] = grade
            print("Grade has been updated.")
        else:
            print(f"Student is not registered to {course_id}")
        
    
     
    


def get_courses():
    global courses
    print("Courses Offered")
    for c,n in courses.items():
        print(c,":",n)

def view_report(students):
    
    s = "None"
    while(s =="None"):
        rollno = input("Enter Rollno To get Rec: or 0 to exit: ")
        if(rollno == "0"):
            return
        s = students.get_student(rollno)
    print("     Student Details")
    print(f"{s.rollno} | {s.name} | {s.age} | {s.gender}")
    print("     Registered Courses")
    ls = s.registered_courses
    for c in ls:
        print(c,":",courses[c])

    if rollno in Grades:
        print("     Transcript")
        for c_id,grade in Grades[rollno].items():
            print(courses[c_id], ": ", grade if grade else 'I')
    

    if rollno in attendance:
        print("     Attendance Details")

        for c_id, date in attendance[rollno].items():
            print(courses[c_id], ":" ,end='')
            for day in date:
                print(day," ",end='')
            print('')
    else:
        print("No Record Found")

def save(students):
    with open("Grades.json",'w') as file:
        json.dump(Grades,file, indent=4)
    with open("Attendance.json",'w') as file:
        json.dump(attendance,file, indent=4)
    with open("Courses.json",'w') as file:
        json.dump(courses,file, indent=4)
    with open("Students.json",'w') as file:
        student_data = students.get_dict()
        json.dump(student_data,file, indent=4)



def load(students):
    global attendance,Grades,courses
    with open('Attendance.json','r') as file:
        attendance = json.load(file)
    with open('Grades.json','r') as file:
        Grades = json.load(file)
    with open('Courses.json','r') as file:
        courses = json.load(file)
    with open("Students.json",'r') as file:
        student_ls = json.load(file)
        print(student_ls)
        for s in student_ls:
            student =  Student(s["name"],s["rollno"],s["age"],s["gender"])
            #print(s["name"])
            student.registered_courses = s["registered_courses"]
            students.add_student(student)
        
    
    

# student = Student("Talib","21F-9070",22,"Male")
# students = CustomList()
# students.add_student(student)
# enroll_student(student=student,course_id="CS1001")
# print(Grades)
# add_grades(students)
# mark_attendance(students)
# view_report(students)
# for student in s:
#     print(student.name,student.rollno,student.registered_courses)

# s1 = students.get_student("21F-9070")
# print(s1.registered_courses)
# enroll_student(course_id="CS1007",student=s1)
# enroll_student(course_id="CS1003",student=s1)

# print(s1.registered_courses)

# print(courses)
# add_course(course_id="CS1002",course_name="OOP")

# print(courses)

# def get_courses():
#     print("Courses List")
#     for id,name in courses.items():
#         print(id,":",name)



if __name__== "__main__":
    students = CustomList()
    while(True):
        print("1.Add Student\n2.View All Student\n3.Add Course\n4.Enroll Student\n5.Mark Attendace\n6.Add Grades\n7.View Student Report\n8.Save Records\n9.Load Records\n10.Exit")
        case = int(input("Choose an option: "))
        os.system("cls")
        match case:
            case 1:
                print("Adding a new Student")
                name = input("Enter Student Name: ")
                rollno =  input("Enter Rollno: ")
                gender =  input("Enter Student Gender: ")
                age = int(input("Enter Student Age: "))
                student = Student(name,rollno,age,gender)
                students.add_student(student)
                print("New Student Added Successfully")
                os.system("pause")
            case 2:
               student_list =  students.view_all_students()
               if(student_list):
                    print("All Student Details\n")
                    for s in student_list:
                         print(f"Name: {s.name} | Rollno: {s.rollno} | Age: {s.age} |Gender: {s.gender} | Regisitered Courses {s.registered_courses}")
               else:
                   print("No student exist")
               print("Student Record Fetched Successfully")
               os.system("pause")

            case 3:
                get_courses()
                print("Enter Course Details")
                c_id = input("Enter Course ID: ")
                c_name = input("Enter Course Name: ")
                add_course(course_id=c_id,course_name=c_name)
                print("Courses Added Successfully")
                os.system("pause")
            case 4: 
                print("Enter below details to enroll student")
                student_rollno = input("Enter Rollno: ")
                s = students.get_student(student_rollno)
                if s == "None":
                    continue
                get_courses()
                course_id = input("Enter Course ID: ")
                enroll_student(student=s,course_id=course_id)
            case 5:
                mark_attendance(students)
                print("Attendance Marked Successfully")
                os.system("pause")
            case 6:
                add_grades(students)
            case 7:
                view_report(students)
                print("Report has been generated Successfully")
                os.system("pause")
            case 8:
                save(students)
                print("Data Saved Successfully")
                os.system("pause")
            case 9:
                load(students)
                print("Data Loaded Successfully")
                os.system("pause")
            case 10:
                save(students)
                print("Data Saved Successfully")
                os.system("pause")
                print("\nThank you for using Student Management System \nDeveloped with ❤ by Talib")
                os.system("pause")
                exit()
            case _:
                print("Invalid Choice")
        os.system("cls")
            


