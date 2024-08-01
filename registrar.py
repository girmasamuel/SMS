import csv
import random,string

stud_path = "database/student_profile.csv"
lec_path =  "database/lecturers_profile.csv"

def asign_section():
    count = 0 
    existing_section = {}
    with open(stud_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if row['section'] not in existing_section:
                existing_section[row['section']] = 1
            else:
                count = existing_section[row['section']] + 1
                existing_section[row['section']] = count
    if existing_section == {}:
        return 1
    else:
        for section,numbers in existing_section.items():
            if numbers <= 2:
                sec = section
                break
            elif numbers > 2:
                sec = int(section)+1
                continue
        return sec  


def default_passwd(portal = '1',path = stud_path):
    if portal == '2':
        path = "database/admin_profile.csv"

    existing_passwords = set()
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            existing_passwords.add(row['password'])
    while True:
        new_password = ''.join(random.choices(string.digits, k=6))
        if new_password not in existing_passwords:
            break
    return new_password

def id(portal):

    if portal in [1,2]:
        if portal == 1:
            prefix = "UGR"
            path = stud_path
        elif portal == 2:
            prefix = "TCR"
            path = lec_path

        existing_id = set()

        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                existing_id.add(row['id_number'])
        while True:
            new_id = f"{prefix}/{''.join(random.choices(string.digits, k=5))}/16"
            if new_id not in existing_id:
                break
        return new_id


    elif portal == 3:
        prefix = "admin"
        path = 'database/admin_profile.csv'

        existing_id = set()
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                existing_id.add(row['username'])
        while True:
            new_id = f"{prefix}{''.join(random.choices(string.digits, k=2))}"
            if new_id not in existing_id:
                break
        return new_id


def stud_store_on_database(students):
    fieldnames = ['full_name', 'id_number', 'section', 'password']

    # Check if the file exists
    try:
        with open(stud_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_students = {row['full_name']: row for row in reader}
    except FileNotFoundError:
        existing_students = {}

    with open(stud_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the column headers if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()
        
        if students.full_name not in existing_students:
            writer.writerow({
                'full_name': students.full_name,
                'id_number': students.ID_no,
                'section': students.section,
                'password': students.password
            })
            existing_students[students.full_name] = True
        else:
            print(f"Student {students.full_name} already exists.")

def lect_store_on_database(lectures):
    fieldnames = ['full_name','id_number','course','password']

    # Check if the file exists
    try:
        with open(lec_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_lecture = {row['full_name']: row for row in reader}
    except FileNotFoundError:
        existing_lecture = {}
    
    with open(lec_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the column headers if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

    
        if lectures.full_name not in existing_lecture:
            writer.writerow({
                'full_name': lectures.full_name,
                'id_number': lectures.id_number,
                'course': lectures.course_lecture,
                'password': lectures.password
            })
            existing_lecture[lectures.full_name] = True
            print("The lecture,registered successfully !")
        else:
            print(f"The lecture Mr.{lectures.full_name} already exist.")
            
#---------------------------------| Add admin |-----------------------------------------------------
def add_admin(admins):
    fieldnames = ['full_name','username','password']

    # Check if the file exists
    try:
        with open(lec_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_admins = {row['username']: row for row in reader}
    except FileNotFoundError:
        existing_admins = {}
    
    with open('database/admin_profile.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the column headers if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        #add new admin to database
        if admins not in existing_admins:
            writer.writerow({
                'full_name': admins,
                'user_name': id(3),
                'password': default_passwd()
            })
            existing_admins[admins] = True
            print("The admin,added successfully !")
        else:
            print(f"The admin username{admins} already exist.")

def dispaly_admin(admin):

    with open('database/admin_profile.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['full_name'] == admin:
                print(f"full name :{row['full_name']}")
                print(f"user name :{row['username']}")
                print(f"password: {row['password']}")
                break  # Stop searching after finding the student
        else:
            print(f"admin {admin} not found.")