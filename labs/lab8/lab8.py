"""
Name: Angie Bui
lab8.py

Problem: Reading and writing files, calculate students average and class average.
Errors if the weight is greater or less than 100.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    student_info = in_file.readlines()
    total_class_avg = 0
    valid_num = 0
    for line in student_info:
        weight = 0
        averages = 0
        total_grade_average = 0
        add_averages = 0
        name = line.split(":")
        first_last_name = name[0]
        # split each numbers by spaces
        student_grades = name[1].strip().split()
        for file_weights in range(0, len(student_grades),2):
        # file_weights location of weight which skips by 2, and add 1 to get the location of the averages
            weight = weight + eval(student_grades[file_weights])
            averages = eval(student_grades[file_weights + 1])
            add_averages = (eval(student_grades[file_weights])*averages) + add_averages
        total_grade_average = total_grade_average + add_averages/100
        if weight < 100:
            averages = "Error: The weights are less than 100 "
        elif weight > 100:
            averages = "Error: The weights are more than 100"
        else:
            total_class_avg = total_class_avg + total_grade_average  # accum for total grade avg
            valid_num = valid_num + 1  # accum for valid num of students
            averages = round(total_grade_average, 1)
        class_avg = total_class_avg / valid_num


        out_file.write(str(first_last_name) + str("'s average: ") + str(averages) + "\n")
    out_file.write(str("Class average: ") + str(class_avg))


    in_file.close()
    out_file.close()
weighted_average("grades.txt","avgs.txt")