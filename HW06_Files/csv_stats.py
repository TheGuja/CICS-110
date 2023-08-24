# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import csv_parse
import csv_split
import basic_io

def get_stats(nums):

    stats = {
        "mean": sum(nums) / len(nums),
        "std_dev": (sum([(num - (sum(nums) / len(nums))) ** 2 for num in nums]) / len(nums)) ** (1/2),
        "min": min(nums),
        "max": max(nums),
        "range": max(nums) - min(nums)
    }

    return stats

def get_assignment_stats(student_info):

    for student in student_info:
        student["scores"] = [float(score) for score in student["scores"]]

    scores_per_student = [(student["scores"]) for student in student_info]

    for i in range(len(scores_per_student)):
        scores_per_student[i].insert(0, student_info[i]["average"])

    scores_per_assignment = []

    for i in range(len(scores_per_student[0])):
        list = []
        for row in scores_per_student:
            list.append(row[i])
        scores_per_assignment.append(list)

    return [get_stats(score) for score in scores_per_assignment]

def write_assignment_stats(fname):

    students = csv_parse.read_csv(fname)

    if students is not None:

        stats = get_assignment_stats(students)
        final_stats = []

        for stat in stats:
            minimum = stat["min"]
            maximum = stat["max"]
            range = stat["range"]
            mean = stat["mean"]
            std_dev = stat["std_dev"]

            list = [minimum, maximum, range, mean, std_dev]
            list_string = [str(element) for element in list]
            final_stats.append(",".join(list_string))

        basic_io.write_lines(f"{fname[:-4]}_stats.csv", final_stats)
    
def write_section_assignment_stats(fname):

    students = csv_parse.read_csv(fname)

    if students is not None:
        sections = {student["section"] for student in students}

        for section in sections:
            current_section = csv_split.filter_section(students, section)
            stats = get_assignment_stats(current_section)

            final_stats = []

            for stat in stats:
                minimum = stat["min"]
                maximum = stat["max"]
                range = stat["range"]
                mean = stat["mean"]
                std_dev = stat["std_dev"]

                list = [minimum, maximum, range, mean, std_dev]
                list_string = [str(element) for element in list]
                final_stats.append(",".join(list_string))

            basic_io.write_lines(f"{fname[:-4]}_section_{section}_stats.csv", final_stats)