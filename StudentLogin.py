def StudentMenu():
    student_courses=[]
    StudentDashBoard(student_courses)
def student_view_courses(student_courses):
    print("****************************************************************************")
    print("*....................Course Details........................................*")
    print("*.....I can help you to give course details here..select your sector.......*")
    print("*..........................................................................*")
    print("****************************************************************************")
    branches=["CSE/IT","ECE","EEE","MECH","CIVIL"]
    for i in range(len(branches)):
        print("{}.{}".format(i+1,branches[i]))
    print("\nSelect Your Branch: ",end="")
    branch_no=int(input())
    try:
        if branch_no>0 and branch_no<6:
            branch_courses(branch_no,student_courses)
        else:
            print("\nPlease enter valid input")
            student_view_courses(student_courses)
    except Exception as e:
        print("Please enter valid input")
        student_view_courses(student_courses)
def StudentDashBoard(student_courses):
    try :
        print("\n****************************\n")
        print("*........DashBoard.........*\n")
        print("*please choose the option :*\n")
        print("*1. Enroll courses         *\n")
        print("*2. Registered Courses     * \n")
        print("*3. Delete existing courses*\n")
        print("*4. Quit                   *\n")
        option = int(input("****************************\n"))
        if option==1 :
            student_view_courses(student_courses)
        elif option==2:
            if student_courses==[]:
                print("\nYou are not yet enrolled to any course....")
                StudentDashBoard(student_courses)
            else:
                print("\nYour Courses: ",end="")
                print(student_courses)
                StudentDashBoard(student_courses)
        elif option==3:
            delete_courses(student_courses)
        elif option==4:
            quit()
        else :
            print("\nplease enter valid option\n")
            StudentDashBoard(student_courses)
    except Exception as e :
        print("Please enter valid input")
        StudentDashBoard(student_courses)
def branch_courses(branch_no,student_courses):
    cse_courses=["Machine Learning","Web Development","Game Development","Data Science"]
    ece=["VLSI","IOT","Optical Networks","Embedded Systems"]
    eee=["Java Programming","Power Systems","Robotics","IOT"]
    mech=["Engineering Mechanics","Robotics","Python Programming",'IOT']
    civil=["Construction Management","C++ Programming","C Programming","Java Programming"]
    all_courses=[cse_courses,ece,eee,mech,civil]
    branch_name=['CSE/IT','ECE','EEE','MECH','CIVIL']
    count=1
    print()
    for k in all_courses[branch_no-1]:
        print("{}. {}".format(count,k))
        count+=1
    print("\nSelect Your {} Courses: \n\nEnter 5 to go back to DashBoard \n\n".format(branch_name[branch_no-1]),end=" ")
    selected_course=int(input())
    if selected_course==5:
        StudentDashBoard(student_courses)
    elif selected_course>0 and selected_course<5:
        if all_courses[branch_no-1][selected_course-1] not in student_courses:
            print("Your are successfully enrolled in {}".format(all_courses[branch_no-1][selected_course-1]))
            student_courses.append(all_courses[branch_no-1][selected_course-1])
        else:
            print("\nYou are already enrolled in that course...")
    student_course_details(student_courses)
def student_course_details(student_courses):
    print("...................................")
    print("Your Registered Courses: ",end="")
    print(student_courses)
    StudentDashBoard(student_courses)
def delete_courses(student_courses):
    if student_courses==[]:
        print("\n\nYou are not enrolled to any course..\n\n")
        StudentDashBoard(student_courses)
    print("\nYour Courses are: ")
    for k in range(len(student_courses)):
        print("{}. {}".format(k+1,student_courses[k]))
    try:
        course_to_delete=int(input("\nEnter 0 to go back\nWhich course you want to delete: "))
        if course_to_delete==0:
          StudentDashBoard(student_courses)
        else:
          student_courses.remove(student_courses[course_to_delete-1])
          if student_courses==[]:
            print("You have not enrolled to any course")
          else:
            print("\nNow your Courses are: ",end="")
            print(student_courses)
        StudentDashBoard(student_courses)
    except Exception as e:
        print("\nEnter Valid Input")
        delete_courses(student_courses)
def quit():
    print("Thank You!!!")
    print("...................................")
