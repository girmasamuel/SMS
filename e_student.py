import csv
import registrar

path = "database/student_profile.csv"

class Student:
    def __init__(self,full_name,section=registrar.asign_section(),ID_no = registrar.id(1),password = registrar.default_passwd()):
        self.full_name = full_name
        self.ID_no = ID_no
        self.section = section
        self.password = password

def display_student_info(student_id):
    try:
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id_number'] == student_id:
                    print(f"Student ID: {row['id_number']}")
                    print(f"Name: {row['full_name']}")
                    print(f"Section: {row['section']}")
                    break  # Stop searching after finding the student
            else:
                print(f"Student with ID {student_id} not found.")
    except FileNotFoundError:
        print(f"CSV file '{path}' not found.")

def display(full_name):
    try:
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['full_name'] == full_name:
                    print(f"Student ID: {row['id_number']}")
                    print(f"Name: {row['full_name']}")
                    print(f"Section: {row['section']}")
                    print(f"password: {row['password']}")
                    break  # Stop searching after finding the student
            else:
                print(f"Student {full_name} not found.")
    except FileNotFoundError:
        print(f"CSV file '{path}' not found.")



