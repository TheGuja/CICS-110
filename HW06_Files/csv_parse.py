# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import basic_io

def read_csv(fname):

    list = []
    lines = basic_io.read_lines(fname)
    
    if lines is not None:
        for line in lines:

            line = line.split(",")
            numbers_string = line[2:]
            numbers_integers = [float(num) for num in numbers_string]
            average = round(sum(numbers_integers) / len(numbers_integers), 3)

            dictionary = {
                "name": line[0],
                "section": line[1],
                "average": average,
                "scores": numbers_integers
            }

            list.append(dictionary)

        return list

def write_csv(fname, student_list):

    information = []

    for student in student_list:

        name = student["name"]
        section = student["section"]
        scores = student["scores"]
        string_scores = ",".join([str(score) for score in scores])

        students = [name, section, string_scores]
        information.append(",".join(students))

    basic_io.write_lines(fname, information)