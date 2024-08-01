import csv
import os
import registrar
import grade_operation
import graphics
stud_path = "database/student_profile.csv"
lec_path = "database/lecturers_profile.csv"

class Teacher:
   def __init__(self,full_name,course_lecture = '',id_number = registrar.id(2),section = [], password = registrar.default_passwd()):
      self.full_name = full_name
      self.id_number = id_number
      self.course_lecture = course_lecture
      self.password = password
      self.section = section


def organize_students_by_section__and_give_score(output_folder,sec_lis,key): # after organizing student list give score on given course
                                                                                   
    student_data = {sec_lis:[]}
    with open('database/student_profile.csv', 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            section = row.get('section')
            if section == sec_lis:
                student_data[section].append(row)

    for section, students in student_data.items():
        section_file = output_folder
        with open(section_file, 'w', newline='') as outfile:
            fieldnames = ['full_name', 'ID number', 'score','grade','point']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                full_name = student.get('full_name', '')  # Get full name
                student_id = student.get('id_number', '')  # Get ID number

                print(f"Enter score for: {full_name} (ID: {student_id})")
                while True:
                    try:
                        score = input("Score: ")
                        if score == '':  # Allow blank input
                            break
                        score = float(score)  # Convert to float if not blank
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number or leave blank.")

                #row['score'] = score
                writer.writerow({
                    'full_name': f"{student.get('full_name')}",
                    'ID number': f"{student.get('id_number')}",
                    'score': score,
                    'grade': grade_operation.grade(score)[0],
                    'point': grade_operation.grade(score)[1] * grade_operation.course_list[key][1]
                })


def display_student_lis(sub_path):
    
    with open(sub_path, 'r') as file:
        reader = csv.reader(file)

        # Find the maximum width for each column
        column_widths = []
        for row in reader:
            for i, value in enumerate(row):
                if i >= len(column_widths):
                    column_widths.append(len(value))
                else:
                    column_widths[i] = max(column_widths[i], len(value))

        # Move file pointer back to the beginning for printing
        file.seek(0)

        # Print header row
        header = next(reader)
        print("|" + "|".join(f" {value:^{column_widths[i]}} " for i, value in enumerate(header)) + "|")

        # Print separator line
        print("|" + "|".join("-" * (column_widths[i] + 2) for i in range(len(header))) + "|")

        # Print data rows
        for row in reader:
            print("|" + "|".join(f" {value:<{column_widths[i]}} " for i, value in enumerate(row)) + "|")

def display(full_name):
    try:
        with open(lec_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['full_name'] == full_name:
                    print(f"Lectures ID: {row['id_number']}")
                    print(f"Name: Mr. {row['full_name']}")
                    print(f"lecture:  {row['course']}")
                    print(f"password: {row['password']}")
                    break  # Stop searching after finding the student
            else:
                print(f"Student {full_name} not found.")
    except FileNotFoundError:
        print(f"CSV file '{lec_path}' not found.")



def make_directory(directory_path):
  if not os.path.exists(directory_path):
    try:
      os.makedirs(directory_path)
    except OSError as error:
      print(f"Error creating directory {directory_path}: {error}")




