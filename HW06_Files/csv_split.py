# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import csv_parse

def filter_section(student_info, section_string):
    return [student for student in student_info if student["section"] == section_string]
    
def filter_average(student_info, min_inc, max_exc):
    return [student for student in student_info if min_inc <= student["average"] < max_exc]

def split_section(fname):
    
    students = csv_parse.read_csv(fname)

    if students is not None:
        sections = {student["section"] for student in students}

        for section in sections:
            write = [student for student in students if student["section"] == section]
            csv_parse.write_csv(f"{fname[:-4]}_section_{section}.csv", write)

def split_average(fname):

    students = csv_parse.read_csv(fname)

    if students is not None:
        scores = {
            "1": (0, 60),
            "2": (60, 75),
            "3": (75, 85),
            "4": (85, 101)
        }

        for score in scores:
            write = filter_average(students, scores[score][0], scores[score][1])
            csv_parse.write_csv(f"{fname[:-4]}_score_{score}.csv", write)