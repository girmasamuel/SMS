#craeting course object which have attributes course title,course code and credit hour


class lecture:
    def __init__(self,course_title = '',course_code = '',credit_hour = 0):
        self.course_title = course_title
        self.course_code = course_code
        self.credit_hour = credit_hour
  

def grade(score):
    if score in range(90,100):
        grade = "A+"
        point = 4.00
        return grade,point
    elif score in range(85,90):
        grade = "A"
        point = 4.00
        return grade,point
    elif score in range(80,85):
        grade = "A-"
        point = 3.75
        return grade,point 
    elif score in range(75,80):
        grade = "B+"
        point = 3.50
        return grade,point
    elif score in range(70,75):
        grade = "B"
        point = 3.00
        return grade,point
    elif score in range(65,70):
        grade = "B-"
        point = 2.75
        return grade,point 
    elif score in range(60,65):
        grade = "C+"
        point = 2.50
        return grade,point
    elif score in range(50,60):
        grade = "C"
        point = 2.00
        return grade,point
    elif score in range(45,50):
        grade = "C-"
        point = 1.75
        return grade,point 
    elif score in range(40,45):
        grade = "D"
        point = 4.0
        return grade,point
    else:
        grade = "F"
        point = 0.00
        return grade,point
    
#This is first year first semister courses common course:

course1 = lecture('applied mathematics','MATH1101',4)
course2 = lecture('introduction to civics & ethics','LART1001',3 )
course3 = lecture('general chemistry','CHEM1101',3)
course4 = lecture('general physics','Phys1101',3)
course5 = lecture('introduction to computing','CSEg1101',3 )
course6 = lecture('communicative english','EnLa1001',3 )
course7 = lecture('physical fitness and conditioning I','SpSc1011',0)

courses = [course1,course2,course3,course4,course5,course6,course7]

course_list = {'1' : [course1.course_title, course1.credit_hour],
               '2' : [course2.course_title, course2.credit_hour],
               '3' : [course3.course_title, course3.credit_hour],
               '4' : [course4.course_title, course4.credit_hour],
               '5' : [course5.course_title, course5.credit_hour],
               '6' : [course6.course_title, course6.credit_hour],
               '7' : [course7.course_title, course7.credit_hour]}


def print_course():# Print keys and course titles
    for course_id, course_info in course_list.items():
        course_title = course_info[0]  # Extract course title from the list
        print(f"[{course_id}] {course_title}")

