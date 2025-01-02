# Josh Fancher
# Final Project
# Client program

import student_grade_program as student
import matplotlib.pyplot as plt
import time


def main():
    # create list for student objects
    student_list = []

    # populate the list with a few objects - default data for testing purposes
    student_list.append(student.student("josh", "fancher", 123, "11/21/1980", 65, 80, 10, 75))
    student_list.append(student.student("jerry", "t", 111, "1/1/2020", 100, 50, 10, 50))
    student_list.append(student.student("jordan", "h", 777, "01/11/2000", 50, 100, 10, 0))
    student_list.append(student.student("scott", "s", 444, "06/12/1970", 50, 100, 10, 100))
    student_list.append(student.student("samuel", "l", 100, "01/09/1998", 100, 100, 10, 100))

    # display menu
    choice = get_menu_choice()

    ##########################################
    # if choice 1
    # program quits

    while choice != 1:
        ''' ends program when choice 1 is selected '''

        ######################################
        # if menu choice 2

        if choice == 2:
            ''' add a student to program if selected'''
            # get user input
            first_name, last_name, student_ID, date_of_birth, assignment_one, assignment_two, weekly_lab_work, final_exam = get_student_input()
            # create a student object
            new_student = student.student(first_name, last_name, student_ID, date_of_birth, assignment_one,
                                          assignment_two, weekly_lab_work, final_exam)
            # flag variable that will change to "y" if the same student object already exists
            duplicate_student_flag = "n"

            # for loop using our custom object __eq__ method determining if the student object already exists
            for i in student_list:
                if (i == new_student):
                    duplicate_student_flag = "y"
                else:
                    ""
                    # will add student object to list if flag variable is "n" otherwise diplays message
            if duplicate_student_flag == "y":
                print("")
                print("*** Student record already exists - this record will not be added ***")
            else:
                # add student object to list
                student_list.append(new_student)
                print(" - Record added - ")

            print("")
            print("--- Main Menu ---")
            print("")
            # display menu
            choice = get_menu_choice()


        ######################################
        # if menu choice 3

        elif choice == 3:
            # if no students have been added to the list diplay message
            # otherwise display all the student objects entered into the program
            if not student_list:
                print("*** No students have been added to the program ***")
            else:
                # function for marks_caluculation of all student obeject in the list
                average_mark_calculation(student_list)
                print("")
                for i in student_list:
                    print(i)
                    print("")
                print("")

            print("--- Main Menu ---")
            # display menu
            choice = get_menu_choice()

        #######################################
        # if menu choice 4
        # "4 - Compute average overall mark for students currenlty entered in the program"
        elif choice == 4:

            print("")
            # invoke average_mark_calculation function and set the return value to marks_average
            marks_average = average_mark_calculation(student_list)
            print(f"Average overall marks for students currently entered in the program: {marks_average:.2f}")
            print("")
            # display menu
            choice = get_menu_choice()

        ######################################
        # if menu choice 5
        elif choice == 5:
            print("")
            # variables for our count of above and below average students
            count_of_students_below_average = 0
            count_of_students_above_average = 0
            # invoke average_mark_calculation function and set the return value to marks_average
            marks_average = average_mark_calculation(student_list)

            # count number of students below average and average and above
            for i in student_list:
                if i.get_overall_mark() < marks_average:
                    count_of_students_below_average += 1
                else:
                    count_of_students_above_average += 1
            print(f"The number of students scoring below average is: {count_of_students_below_average}")
            print(f"The number of students scoring above avearge or above is: {count_of_students_above_average}")
            print("")
            # diplay menu
            choice = get_menu_choice()


        #######################################
        # if menu choice 6
        # 6 - Display the distribution of grades (ie. number of HD, D's etc.. graphical output)
        # calculate the final grades
        elif choice == 6:
            print("")
            # if no data has been entered into the program print message
            if not student_list:
                print("*** No students have been entered into the program ***")
            else:
                # invoke average_mark_calculation function to ensure overall_marks have been computed
                average_mark_calculation(student_list)
                # variables for our count of each letter grade
                count_HD = 0
                count_D = 0
                count_C = 0
                count_P = 0
                count_N = 0

                # print message before generating graphical output
                # program will stop while output is generating and will not continue
                # until the output is closed
                print("-- Close graphical output to continue --")

                for i in student_list:
                    # our method .final_grade_calculation() calculates the letter grade for each student object
                    i.final_grade_calculation()
                    # if/else to count number of letter grades present in the list of student object
                    if i.get_final_grade() == "HD":
                        count_HD += 1
                    elif i.get_final_grade() == "D":
                        count_D += 1
                    elif i.get_final_grade() == "C":
                        count_C += 1
                    elif i.get_final_grade() == "P":
                        count_P += 1
                    elif i.get_final_grade() == "N":
                        count_N += 1
                    else:
                        ""

            # using matplotlib to print a visualization

            x_coords = [0, 1, 2, 3, 4]
            y_coords = [count_HD, count_D, count_C, count_P, count_N]

            plt.bar(x_coords, y_coords)

            plt.title("Final Grades Histogram")

            plt.xlabel("Final Grade")

            plt.ylabel("Count of Final Grades")

            plt.xticks([0, 1, 2, 3, 4],
                       ["HD", "D", "C", "P", "N"])

            plt.yticks([0, 1, 2, 3, 4],
                       ["0", "1", "2", "3", "4"])
            plt.grid(True)

            plt.show()

            print("")

            # display menu
            choice = get_menu_choice()



        #######################################
        # if menu choice 7
        # "7 - View student details by ID number"

        elif choice == 7:
            # try/except blocks of input validation
            # if student_ID not present in list of student objects statement will except
            try:
                student_ID = int(input("Enter student ID number to view student details: "))
                # flag variable will change to "y" if a student with the matching student_ID is found
                flag = "n"
                for i in student_list:
                    if int(i.get_student_ID()) == student_ID:
                        print("")
                        print(i)
                        flag = "y"
                    else:
                        ""
                # if flag == "n" print message informing user no matching student_ID was found
                if flag == "n":
                    print("*** Student ID not found ***")
                else:
                    ""
            except:
                print("*** Student ID must be a number ***")
                pause = input("--- To return to main menu press [Enter] ")

            print("")
            choice = get_menu_choice()


        #########################################
        # if menu choice 8
        # "8 - View student details by surname and given name"

        elif choice == 8:
            # get user input
            surname = input("Enter student surname: ")
            given_name = input("Enter student given name: ")
            # flag variable to change to "y" if an object is found in the list matching surname and last name
            flag = "n"
            for i in student_list:
                # using our get methods to get the names and setting them to .upper() to ignore case
                if i.get_last_name().upper() == surname.upper() and i.get_first_name().upper() == given_name.upper():
                    print("")
                    print(i)
                    flag = "y"
                else:
                    ""
            # if flag == "n" then print a appropriate error message
            if flag == "n":
                print("")
                print("*** No student found based on surname and given name ***")
            else:
                ""
            print("")

            # display menu
            choice = get_menu_choice()

        ########################################
        # if menu choice 9
        # 9 - Sort students in program by ascending order of students ID numbers - write our own sorting methods - analyze time complexity of algorithm - use example bubble sort
        elif choice == 9:
            # invoke our bubblesort function and sort the list
            # returning the a sorted list and the time it took to sort the list
            sorted_list, time_bubble_sort = bubblesort(student_list)
            print("")
            print(f"Bubble Sort time complexity: {time_bubble_sort} ")
            print("")
            for i in sorted_list:
                print(i)
            print("")
            # display menu
            choice = get_menu_choice()

    # close of program
    print("")
    print("--- Program Closed ---")


def bubblesort(our_list):
    '''arguments - list of student objects
       sorts the list in ascending order
       returns sorted_list, elapsed time of algorithm'''
    # Time complexity analysis
    start = time.time()

    # bubble sort algorithm
    n = len(our_list)
    while n > 1:
        i = 1
        while i < n:
            if our_list[i].get_student_ID() < our_list[i - 1].get_student_ID():
                swap(our_list, i, i - 1)
            i += 1
        n -= 1
    # computing the time to run the bubblesort algorithm
    elapsed = time.time() - start

    return our_list, elapsed


def swap(our_list, i, j):
    # used in our bubblesort
    temp = our_list[i]
    our_list[i] = our_list[j]
    our_list[j] = temp


def average_mark_calculation(student_list):
    ''' arguments - list of student objects
        loops through list of students objects and computes the overall average marks
        for the students in the list
        returns - the overall average
    '''
    # variable to compute our average marks
    average_overall_marks_sum = 0
    average_overall_marks = 0
    for i in student_list:
        # our method .overall_mark_calculation() computes overall_mark for each student object
        i.overall_mark_calculation()

        average_overall_marks_sum += i.get_overall_mark()
    average_overall_marks = average_overall_marks_sum / len(student_list)

    return average_overall_marks


def get_menu_choice():
    '''displays menu options
       validates input for chosen options
    '''
    print("Student Grade Program")
    print("--- Main Menu ---")
    print("1 - Quit (exit the program)")
    print("2 - Add student for grade calculation")
    print("3 - Output details for all students currently entered in the program")
    print("4 - Compute average overall mark for students currenlty entered in the program")
    print("5 - Display number of students equal to or above overall average marks and below")
    print("6 - Display distribution of grades (ie. number of HD, D's etc.. graphical output)")
    print("7 - View student details by ID number")
    print("8 - View student details by surname and given name")
    print("9 - Sort students in program by ascending order of students ID numbers")

    # initialize choice variable
    choice = -1

    # get choice from user
    # input validation if user inputs alpha characters
    print("")
    while choice < 0 or choice > 9:
        # try / except block for input validation if not an integer will except
        try:
            choice = int(input("Enter choice: "))
            if choice < 0 or choice > 9:
                print("*** Please select choice number (1 to 9)")

        except:
            print("*** Invalid Choice ***")
            print("*** Please select choice number (1 to 9) ")

    return choice


def get_student_input():
    '''gets user input'''
    # use the .strip() method to ensure potential white space at the beginning or end
    # of user input is stripped out
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()

    # input validation for numeric student ID
    # initialzie student_ID to -1 and a numeric data type
    student_ID = -1
    while student_ID < 0:
        try:
            student_ID = int(input("Enter Student ID: "))

        except:
            print("*** Please enter a numerical ID number ***")

    # input validation for date of birth
    # set date_of_birth variable to empty string ""
    date_of_birth = ""
    # validation that date of birth has 2 forward slashes the date of birth string must be minimum lenght of 8
    while date_of_birth.count("/") != 2 or len(date_of_birth) < 8:
        date_of_birth = input("Enter date of birth in the format dd/mm/yyyy format: ")
        # try/except to validate input prevent an abrupt halt if user types randomly or out of range error
        try:
            while int(date_of_birth.split("/")[2]) < 1900 or int(date_of_birth.split("/")[2]) > 2022:
                print("The year of birth must be between 1900 and 2022 --")
                date_of_birth = input("Enter date of birth in the format dd/mm/yyyy format: ")
            while int(date_of_birth.split("/")[0]) < 1 or int(date_of_birth.split("/")[0]) > 12:
                print("The month of birth must be between 1 - January and 12 - December --")
                date_of_birth = input("Enter date of birth in the format dd/mm/yyyy format: ")
            while int(date_of_birth.split("/")[1]) < 1 or int(date_of_birth.split("/")[1]) > 31:
                print("The actual day of birth must be between 1 and 31 --")
                date_of_birth = input("Enter date of birth in the format dd/mm/yyyy format: ")

        except:
            print("  Please enter valid date of birth with proper formatting and numeric number ***")

    # input validation for assignment one minimum marks 0 and maximum marks 100:
    assignment_one = -1
    while assignment_one < 0 or assignment_one > 100:
        try:
            assignment_one = int(input("Score for assignment one (0 to 100): "))
            if assignment_one < 0 or assignment_one > 100:
                print("*** Must be a score between 0 and 100 ***")

        except:
            print("*** Must be a score between 0 and 100 ***")

    # input validation for assignment two - minimum marks 0 and maximum marks 1000
    assignment_two = -1
    while assignment_two < 0 or assignment_two > 100:
        try:
            assignment_two = int(input("Score for assignment two (0 to 100): "))
            if assignment_two < 0 or assignment_two > 100:
                print("*** Must be a score between 0 and 100 ***")

        except:
            print("*** Must be a score between 0 and 100 ***")

    # input validatino for weekly lab work - minimum marks 0 maximum marks 10
    weekly_lab_work = -1
    while weekly_lab_work < 0 or weekly_lab_work > 10:
        try:
            weekly_lab_work = int(input("Score for assignment lab work (0 to 10): "))
            if weekly_lab_work < 0 or weekly_lab_work > 10:
                print("*** Must be a score between 0 and 10 ***")

        except:
            print("*** Must be a score between 0 and 10 ***")

    # input validatino for final lab work - minimum marks 0 maximum marks 100
    final_exam = -1
    while final_exam < 0 or final_exam > 100:
        try:
            final_exam = int(input("Score for final exam (0 to 100): "))
            if final_exam < 0 or final_exam > 100:
                print("*** Must be a score between 0 and 100 ***")

        except:
            print("*** Must be a score between 0 and 100 ***")

    return first_name, last_name, student_ID, date_of_birth, assignment_one, assignment_two, weekly_lab_work, final_exam


if __name__ == "__main__":
    main()