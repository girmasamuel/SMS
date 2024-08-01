import getpass,os,sys,time
import accounts
import e_student 
import e_teacher
import grade_operation
import registrar
from graphics import*

#---------------------------------| some important tools |-----------------------------------------------------------

# Function to clear console/terminal
def clear_console():
    if os.name == 'nt': #wheather if the system is windoww
        _ = os.system('cls')
    else: #wheather if the system not window but linux or mac
        _ = os.system('clear')

# Function to get the terminal size
def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)

# Function to print text at the center of the terminal
def centered_text(text):
    rows, columns = get_terminal_size()
    padding = " " * ((columns - len(text)) // 2)
    print(padding + text)


#-------------------------------------------------| STUDENT PORTAL |-----------------------------------------------------
def Estudent():
    clear_console()
    time.sleep(1)
    for i in range(3):
        centered_text(f"{RED}LOGIN")
        
        username = input(f"{WATERBLUE}username: ")
        password = getpass.getpass(prompt = f"{WATERBLUE}password: ")
        
        time.sleep(2)
        clear_console()
        print("Checking...")
        time.sleep(1)
        clear_console()

        if accounts.login('1',username,password):
            print("Loging succefully...")
            time.sleep(1)
            clear_console()
            break
        else:
            if i == 1:
                print("You attempt 2 times! This is your last chance!")
                time.sleep(1)
                clear_console()
                continue
            elif i == 2:
                print("If you have forgotten your password or are yet not registered,Please visit regitster office!")
                time.sleep(1)
                clear_console()
                print("program exiting....")
                time.sleep(1)
                clear_console()
                sys.exit()
            print("Invalid user name or password! Please try again!")
            time.sleep(1)
            clear_console()

    #dispaly student option for student
    while True:
        banner("Estudent Page")
        choice = input(f"{GREEN}choose option:\n"
                    f"{GREEN}[1]{END} {BLUE}view your profile                 {GREEN}[3]{END} {BLUE}Transcript\n"
                    f"{GREEN}[2]{END} {BLUE}Acadamic histry                   {GREEN}[4]{END} {BLUE}Change  your password\n"
                    f"{GREEN}[0]{END} {BLUE}Logout: ")                           

#**************************************| Student profile |***********************************************
        if choice == '1':
                
            clear_console()
            banner("Estudent Page/Student Profile")
            print(f"{PURPLE}----------------------------------------------------{END}")
            e_student.display_student_info(username)
            print(f"{PURPLE}----------------------------------------------------{END}")
            while True:
                choice = input(f"{GREEN}[4]{END} {BLUE}back                   {GREEN}[0]{END} {BLUE}logout: ")
                if choice == '4':
                    clear_console()
                    break
                if choice == '0':
                    clear_console(1)
                    main()
                else:
                    continue
#**************************************| Acadamic History |***********************************************
        elif choice == '2':
            clear_console()
            centered_text(f"{RED}The page is on developemnet {END}")
            time.sleep(2)
            clear_console()
        
#**************************************| Transcript |***********************************************
        elif choice == '3':
            clear_console()
            centered_text(f"{RED}The page is on developemnet{END}")
            time.sleep(2)
            clear_console()

#**************************************| Change password |***********************************************
        elif choice == '4':
            clear_console()
            accounts.change_passwd('1',username)
            time.sleep(3)
            clear_console()
            stream_write(f"{RED}keep you passsword secrately!{END}")
            time.sleep(2)
            clear_console()

#**************************************| Logout |***********************************************
        elif choice == '0':
            clear_console()
            main()
        else:
            clear_console()
            continue


#-------------------------------------------| TEACHERS PAGE |----------------------------------------------------------

def Eteacher(lecture,key,section):

    for i in range(3):
        clear_console()
        centered_text(f"{RED}LOGIN{END}")
        username = input(f"{BLUE}username: ")
        password = getpass.getpass(prompt = "password: ")

        clear_console()
        print("chaking...")
        time.sleep(1)

        if accounts.login('2',username,password,lecture):
            clear_console()
            print("Login successful...")
            time.sleep(1)
            clear_console()
            break
        else:
            if i == 1:
                clear_console()
                print("You attempt 2 times! This is your last chance!")
                time.sleep(1)
                clear_console()
                continue
            
            elif i == 2:
                clear_console()
                print("This login error may arise one of the following cause:\n"
                      "    -if you forgot your password\n"
                      "    -if not matched your password and username with password and username stored in database\n"
                      "    -if the course_title you inserted not your course")
                time.sleep(5)
                clear_console()
                print("program exiting, Try agin....")
                time.sleep(2)
                clear_console()
                sys.exit()
            clear_console()
            print("Invalid user name or password! Please try again!")
            time.sleep(1)
            clear_console()

    while True:
        banner("Eteacher Page")
        choice = input(f"{GREEN}Choose your option:\n"
                    f"{GREEN}[1]{END} {BLUE}Add students grade\n"
                    f"{GREEN}[2]{END} {BLUE}display students\n"
                    f"{GREEN}[3]{END} {BLUE}change your password\n"
                    f"{GREEN}[0]{END} {BLUE}Logut: ")

        if choice in ['1','2']:
            clear_console()
            sub_dir = f"database/teachers_mark_list/{lecture}"
            e_teacher.make_directory(sub_dir)
            while True:
                try:
                    sec_num = input(f"enter the section number{section}: ")
                    break
                except:
                    print(f"please enter only from those {section}")

            subj_path = f"{sub_dir}/section_{section[section.index(sec_num)]}.csv"
            if choice == '1':
                
                e_teacher.organize_students_by_section__and_give_score(subj_path,section[section.index(sec_num)],key)
                clear_console()
                print(f"{BLUE}You set score for your students succesfully\n"
                      f"you can see the mark list in {RED}\"display students\"{END}{BLUE} option")
                time.sleep(3)
                clear_console()

            else:
                
                clear_console()    
                print(f"{BLUE}---------------------| {YELLOW}Student list {BLUE}|-------------------{END}")
                try:                         
                    e_teacher.display_student_lis(subj_path) 
                except:
                    print(f"Students of section {sec_num} not organized yet")
                print(f"{BLUE}--------------------------------------------------------{END}")
                                

                choice = input(f"{GREEN}[1] {BLUE}Back                     {GREEN}[0] {BLUE} logout:  ")
                while True:  
                    if choice == '1':
                        clear_console()
                        break
                    elif choice == '0':
                        clear_console()
                        time.sleep(1)
                        main()
                    else:
                        continue        

        elif choice == '3':
            clear_console()
            accounts.change_passwd(2,username)
            time.sleep(2)
            clear_console()
            stream_write(f"{RED}keep you passsword secrately!{END}")
            time.sleep(2)
            clear_console() 

        elif choice == '0':
            clear_console()
            time.sleep(2)
            clear_console()
            time.sleep(1.5)
            main()

        else:
            clear_console()
            continue

#--------------------------------------------------------| Registrar Page |-------------------------------------------------------        
def Registrar():
    clear_console()
    time.sleep(1)
    for i in range(3):
        centered_text(f"{RED}ADMIN LOGIN")
        
        username = input(f"{WATERBLUE}username: ")
        password = getpass.getpass(prompt = f"{WATERBLUE}password: ")
        clear_console()
        print("Checking...")
        time.sleep(1)
        clear_console()

        if accounts.login('3',username,password):
            print("Loging succefully...")
            time.sleep(1)
            clear_console()
            break
        else:
            if i == 1:
                print("You attempt 2 times! This is your last chance!")
                time.sleep(1)
                clear_console()
                continue

            elif i == 2:
                clear_console()
                print("if you change your password.try to remeber")
                print("program exiting....")
                time.sleep(1)
                clear_console()
                sys.exit()
            print("Invalid user name or password! Please try again!")
            time.sleep(1)
            clear_console()
    while True:
        banner("Registrar Page")
        choice = input(f"{GREEN}choose your option:\n"
                    f"{GREEN}[1] {BLUE}Register new lecture\n"
                    f"{GREEN}[2] {BLUE}Password recovery\n"
                    f"{GREEN}[3] {BLUE}Add admin\n"
                    f"{GREEN}[4] {BLUE}Change admin password\n"
                    f"{GREEN}[0]{END} {BLUE}Logout: ")

        if choice == '1':
            while True:
                clear_console()

                name = input(f"Enter lectures full name: {GREEN}")
                clear_console()
                print(f"{BLUE}choose the course:")
                grade_operation.print_course()

                while True:
                    try:
                        key = input(": ")
                        course = grade_operation.course_list[key][0]
                        break
                    except:
                        print("Your choise must only be between(1-7)",end='\r')
                        time.sleep(2)
                        print("                                   ",end='\r')
                lecture = e_teacher.Teacher(name,course)
                
                registrar.lect_store_on_database(lecture)
                time.sleep(2)
                clear_console()
                
            
                print(f"{BLUE}--------------{GREEN}lectures info{BLUE}----------------------")
                e_teacher.display(name)
                print(f"{BLUE}------------------------------------------")
                choice = input(f"{GREEN}[1] {BLUE}Next                         {GREEN}[2] {BLUE}Finished: {GREEN}")
                if choice == '1':
                    clear_console()
                elif choice == '2':
                    clear_console()
                    break

        elif choice == '2':
            clear_console()
            portal = input(f"{GREEN}Choose\n"
                           f"{GREEN}[1] {BLUE}Student\n"
                           f"{GREEN}[2] {BLUE}Teacher: ")
            clear_console()
            time.sleep(1)

            IdNumber = input(f"Enter ID number: {GREEN}")
            clear_console()

            time.sleep(2)
            clear_console()
            
            accounts.change_passwd(portal,IdNumber)
            clear_console()

        elif choice == '3':
            clear_console()
            while True:
                admin = input("Enter admins full name: ")
                registrar.add_admin(admin)
                time.sleep(3)
                clear_console()
                registrar.dispaly_admin(admin)

                choice = input(f"{GREEN}[1] {BLUE}Next               {GREEN}[2] {BLUE}Fimished: ")
                if choice == '1':
                    continue
                elif choice == '2':
                    clear_console()
                    break

        elif choice == '4':
            clear_console()
            accounts.change_passwd(3,username)
            time.sleep(2)
            clear_console()
        elif choice == '0':
            clear_console()
            main()
        else :
            continue

#----------------------------------| HOME PAGGE |-------------------------------------------------------
clear_console()
print(f"{BLUE}System is loading...")
time.sleep(2)
clear_console()


def main():
    while True:

        banner("Homepage")
        portal = input(f"{GREEN}Choose a portal number :\n"
                                f"{GREEN}[1] {BLUE}Estudent\n"
                                f"{GREEN}[2] {BLUE}Eteacher\n"
                                f"{GREEN}[3] {BLUE}Registrar\n"
                                f"{GREEN}[4] {BLUE}New Registration\n"
                                f"{GREEN}[0] {BLUE}Close: ")
        if portal not in ["1","2","3","4","0"] :
            clear_console()
            time.sleep(1)

        else:
            clear_console()
            break  

# redirect to choosen portal
#----------------------------------------| students portal |-----------------------------------------

    if portal == "1":
        clear_console()
        Estudent()
#----------------------------------------| Teachers portal |-----------------------------------------
    elif portal == "2":
        clear_console()
        print(f"Choose your course")

        print(f"{BLUE}---------------------------------------------{GREEN}")
        grade_operation.print_course()
        print(f"{BLUE}---------------------------------------------{END}")
        print(f"{RED}WARNNING{END}: {BLUE}the course must be registered for you.It uses for later login!{END}")

        while True:
            try:
                key = input(": ")
                course = grade_operation.course_list[key][0]
                break
            except:
                print("Your choise must be in number (1-7)",end='\r')
                time.sleep(2)
                print("                                   ",end='\r')


                
        clear_console()
        time.sleep(1)
        section = input(f"{BLUE}enter the section you teach by separating with comma: ").split(sep=",")
        Eteacher(course,key,section = section)

#----------------------------------------| admin portal |-----------------------------------------
    elif portal == "3":
        clear_console()
        Registrar()
#----------------------------------------| Registration  |-------------------------------------------
    elif portal == "4":

        while True:
                clear_console()
                name = input("Enter your full name: ")
               
                student = e_student.Student(name)
                registrar.stud_store_on_database(student)

                time.sleep(2)
                clear_console()
            
                print('Student information')
                print(f"{BLUE}------------------------------------------{END}")
                e_student.display(name)
                print(f"{RED}WARNNING: {GREEN}Don't forget to change deffault password")
                print(f"{BLUE}------------------------------------------{END}")
                choice = input(f"{GREEN}[1] {BLUE}Back to menu                        {GREEN}[2] {BLUE}close: ")

                if choice == '1':
                    time.sleep(1)
                    clear_console()
                    main()
                elif choice == '2':
                    time.sleep(1)
                    clear_console()
                    sys.exit()

#---------------------------------------------------------------------------------------------------
    elif portal == "0":
        clear_console()
        print("the system is existing...")
        time.sleep(2)
        clear_console()
        sys.exit()


if __name__ == '__main__':
    main()