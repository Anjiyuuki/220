from Die import*
from Student import*

def main():
    numbers_of_sides = eval(input('How many sides?'))
    my_die = Die(numbers_of_sides)
    playing = True
    while playing:
        my_die.roll()
        print(my_die.get_value())
        stopping = input('keep playing?')
        playing = not stopping

def g_average():
    my_student = Student("Joe", 8, 12)
    print(my_student.get_gpa())
    # or if it's from a spreadsheet, go to download, click "comma separated values"
    student_file = open('student.txt', 'r')
    student_file.readline()
    # store student rather than overriding each loop
    students_list = []
    for line in student_file.readline():
        # create each student
        name, credit_hours, q_points = line.split(',')
        # split_line = line.split(",")
        # name = split_line[0]
        # credit_hours = split_line[1]
        # q_points = split_line[2]
        student = Student(name, float(credit_hours), q_points)
        students_list.append(student)
    for each_student in students_list:
        print(each_student.get_name())
        print(each_student.get_gpa())

    print(line)



if __name__ == '__main__':
    #main()
    g_average()

