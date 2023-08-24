# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def compute_quizzes(quiz_scores):

    total = sum(quiz_scores)

    if total <= 250:
        return 1
    elif total <= 500:
        return 2
    elif total <= 750:
        return 3
    elif total <= 1000:
        return 4

def compute_midterm(midterm_scores):

    if midterm_scores <= 20:
        return 1
    elif midterm_scores <= 45:
        return 2
    elif midterm_scores <= 80:
        return 3
    elif midterm_scores <= 100:
        return 4
    
def compute_final(final_scores):

    if final_scores <= 25:
        return 1
    elif final_scores <= 50:
        return 2
    elif final_scores <= 75:
        return 3
    elif final_scores <= 100:
        return 4
    
def compute_homework(hw_scores):

    total = sum(hw_scores)

    if total <= 330:
        return 1
    elif total <= 440:
        return 2
    elif total <= 650:
        return 3
    elif total <= 1000:
        return 4
    
def compute_project(proj_scores):
    
    total = sum(proj_scores)

    if total <= 150:
        return 1
    elif total <= 210:
        return 2
    elif total <= 270:
        return 3
    elif total <= 300:
        return 4
    
def compute_lab(lab_scores):
    
    total = sum(lab_scores)

    if total <= 250:
        return 1
    elif total <= 500:
        return 2
    elif total <= 750:
        return 3
    elif total <= 1000:
        return 4
    
def compute_participation(part_scores):

    total = sum(part_scores)

    if total <= 250:
        return 1
    elif total <= 400:
        return 2
    elif total <= 600:
        return 3
    elif total <= 1000:
        return 4
    
def get_cumulative(student):
    
    weighted_quizzes = (compute_quizzes(student[2]) / 4) * 10
    weighted_midterm = (compute_midterm(student[3]) / 4) * 15
    weighted_final = (compute_final(student[4]) / 4) * 15
    weighted_hw = (compute_homework(student[5]) / 4) * 20
    weighted_project = (compute_project(student[6]) / 4) * 20
    weighted_labs = (compute_lab(student[7]) / 4) * 10
    weighted_particiaption = (compute_participation(student[8]) / 4) * 10

    cumulative_weighted_score = weighted_quizzes + weighted_midterm + weighted_final + weighted_hw + weighted_project + weighted_labs + weighted_particiaption

    return cumulative_weighted_score

def determine_grade(cumulative_score, weights):

    if cumulative_score >= weights[0]:
        return "A"
    elif cumulative_score >= weights[1]:
        return "A-"
    elif cumulative_score >= weights[2]:
        return "B+"
    elif cumulative_score >= weights[3]:
        return "B"
    elif cumulative_score >= weights[4]:
        return "B-"
    elif cumulative_score >= weights[5]:
        return "C+"
    elif cumulative_score >= weights[6]:
        return "C"
    elif cumulative_score >= weights[7]:
        return "C-"
    elif cumulative_score >= weights[8]:
        return "D"
    else:
        return "F"

def print_report(student, weights):

    student_name = student[0]
    weighted_cumulative_score = get_cumulative(student)
    final_grade = determine_grade(weighted_cumulative_score, weights)

    print(f"Name: {student_name}\n"
          f"Cumulative: {weighted_cumulative_score}\n"
          f"Final Grade: {final_grade}")
