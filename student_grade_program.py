# Josh Fancher
# Final Project
# Question 3
# CS5001, Fall 2022
# File name: student_grade_program.py
# 12/13/2022


# Design, write in python, test and document (at least) two classes - as student class
# and a client program, as follows:
# - Write a python class called student which can be used to represent the details of
# - a student together with some associated operations. The Student class will have the
# - following information.

# a.) A frist name (give name)
# b.) a last name (family name/surname)
# c.) student number (ID)
# d.) A date of birth (in day/month/year format)
# e.) There are tow assignments, each marked out of a maximum of 100 marks and
#     equally weighted. The marks for each assignment are recoreded separately.
# f.) There is weekly lab work. The marks for this component are recorded as a total
#     mark obtained (out of a maximum of 10 marks) for all lab work demonstrated during the semester
# g.) there is one final examination that is marked out of a maxiumum of 100 marks and recoreded separatel.
# h.) An overall mark (to be calculated within the program)
# i.) A final grade, which is a string (to be calculated within the program)

class student:
    def __init__(self, first_name, last_name, student_ID, date_of_birth, assignment_one, assignment_two,
                 weekly_lab_work, final_exam):
        '''arguments - first_name, last_name, student_ID, date_of_birth, assignment_one, assignment_two, weekly_lab_work, final_exam'''
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_ID = student_ID
        self.__date_of_birth = date_of_birth
        self.__assignment_one = assignment_one
        self.__assignment_two = assignment_two
        self.__weekly_lab_work = weekly_lab_work
        self.__final_exam = final_exam
        self.__overall_mark = 0
        self.__final_grade = ""

    def overall_mark_calculation(self):
        # overall mark calculation
        # potential marks is the maximum score possible on each assignment
        self.__total_potential_marks_assignment_one = 100
        self.__total_potential_marks_assignment_two = 100
        self.__total_potential_marks_lab_work = 10
        self.__total_potential_marks_final_exam = 100
        # weights - are percentage weights associated with each assignment
        # total precentage weights is equal to 100
        self.__assignment_one_weight = 20
        self.__assignment_two_weight = 20
        self.__lab_work_weight = 10
        self.__final_exam_weight = 50
        # calculates the overall mark for the students
        # equation for overall_marks:
        # overall_mark = sum of all equations (acutal marks / maximum potential) * assignment weight)
        self.__overall_mark = (
                                          self.__assignment_one / self.__total_potential_marks_assignment_one) * self.__assignment_one_weight \
                              + (
                                          self.__assignment_two / self.__total_potential_marks_assignment_two) * self.__assignment_two_weight \
                              + (
                                          self.__weekly_lab_work / self.__total_potential_marks_lab_work) * self.__lab_work_weight \
                              + (self.__final_exam / self.__total_potential_marks_final_exam) * self.__final_exam_weight

    def final_grade_calculation(self):
        # caluculates a letters grade based on the overall_mark_calculation
        if self.__overall_mark >= 80:
            self.__final_grade = "HD"
        elif self.__overall_mark >= 70:
            self.__final_grade = "D"
        elif self.__overall_mark >= 60:
            self.__final_grade = "C"
        elif self.__overall_mark >= 50:
            self.__final_grade = "P"
        else:
            self.__final_grade = "N"

    # getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_student_ID(self):
        return self.__student_ID

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_assignment_one(self):
        return self.__assignment_one

    def get_assignment_two(self):
        return self.__assignment_two

    def get_weekly_lab_work(self):
        return self.__weekly_lab_work

    def get_final_exam(self):
        return self.__final_exam

    def get_overall_mark(self):
        return self.__overall_mark

    def get_final_grade(self):
        return self.__final_grade

    # setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_student_ID(self, student_ID):
        self.__student_ID = student_ID

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_assignment_one(self, assignment_one):
        self.__assignment_one = assignment_one

    def set_assignment_two(self, assignment_two):
        self.__assignment_two = assignment_two

    def set_weekly_lab_work(self, weekly_lab_work):
        self.__weekly_lab_work = weekly_lab_work

    def set_final_exam(self, final_exam):
        self.__final_exam = final_exam

    def set_overall_mark(self, overall_mark):
        self.__overall_mark = overall_mark

    def set_final_grade(self, final_grade):
        self.__final_grade = final_grade

    # string method
    def __str__(self):
        # overloading the string method enabling us to print the
        # current state of a student object
        return f"First name: {self.get_first_name()}\n" + \
            f"Last name: {self.get_last_name()}\n" + \
            f"Student ID: {self.get_student_ID()}\n" + \
            f"Date of birth: {self.get_date_of_birth()}\n" + \
            f"Assignment one grade: {self.get_assignment_one()}\n" + \
            f"Assignment two grade : {self.get_assignment_two()}\n" + \
            f"Weekly lab work: {self.get_weekly_lab_work()}\n" + \
            f"Final exam score: {self.get_final_exam()}\n" + \
            f"Overall mark: {self.get_overall_mark()}\n" + \
            f"Final grade: {self.get_final_grade()}\n"

    def __eq__(self, other):
        # overloading the __eq__ method enabling us to compare
        # objects of the student type with the == operator
        # to return true the object must be itself or
        # it must have the same first_name, last_name, student_ID, and date_of_birth
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.__first_name == other.__first_name and \
                self.__last_name == other.__last_name and \
                self.__student_ID == other.__student_ID and \
                self.__date_of_birth == other.__date_of_birth

            # def is_eq_to(self, other):
    #     if self is other:
    #         return True
    #     elif type(self) != type(other):
    #         return False
    #     else:
    #         return self.__first_name == other.__first_name \
    #                and self.__last_name == other.__last_name \
    #                and self.__student_ID == other.__student_ID \
    #                and self.__date_of_birth == other.__date_of_birth
