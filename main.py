from grading import is_valid_score, classify_score, grade_letter
from report_writer import build_report, save_report

try:
    student_name = input("Enter student name: ").strip()
    if student_name == "":
        print("Student name cannot be empty.")
    else:
        score = float(input("Enter student score from 0 to 100: "))
        if not is_valid_score(score):
            print("Score must be between 0 and 100.")
        else:
            status = classify_score(score)
            letter = grade_letter(score)  # Calculate grade letter
            report = build_report(student_name, score, status, letter)
            filename = save_report(student_name, report)
            print(report)
            print(f"Report saved to: {filename}")
except ValueError:
    print("Invalid input. Score must be a number.")
    