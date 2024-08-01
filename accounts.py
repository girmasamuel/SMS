import csv
from graphics import (RED,
                      BLUE,
                      GREEN,
                      YELLOW,
                      PURPLE,
                      WATERBLUE,
                      END)

#Function returns boolean true if user input matches with exiting in database
def login(portal,username, password,lecture = ''):
    if portal == '1':
        with open("database/student_profile.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id_number'] == username and row['password'] == password :
                    return True
        return False

    elif portal == '2':
        with open("database/lecturers_profile.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id_number'] == username and row['password'] == password and row['course'] == lecture :
                    return True
        return False
    
    elif portal == '3':
        with open("database/admin_profile.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['username'] == username and row['password'] == password :
                    return True
        return False
        

def change_passwd(portal,id_number):

    password = input("enter new password: ")
    while True:
        confirm = input("enter new password again: ")
        if password != confirm:
            print("your confirmation password is not matched!")
        else:
            break

    updated_rows = []
    found_student = False  # Flag to track if the student ID is found

    if portal in ['1','2']:

        if portal == '1':
            path = "database/student_profile.csv"
            person = "Student"

        elif portal == '2':
            path = "database/lecturers_profile.csv"
            person = "Lecture"
        

        with open(path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['id_number'] == id_number:
                        row['password'] = password
                        found_student = True
                    updated_rows.append(row)


    else :
        path = "database/admin_profile.csv"
        person = "Registrar"

        with open(path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['username'] == id_number:
                        row['password'] = password
                        found_student = True
                    updated_rows.append(row)


    if not found_student:
        print(f"{RED}Error:{BLUE}{person} with username {RED}'{id_number}'{BLUE} not found.")
    else:
        with open(path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)
            print("Password  changed successfully!\n"
                f"Your new password is {password}")
    
