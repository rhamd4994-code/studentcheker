def build_report(student_name, score, status, letter):
    report = f"""Student Performance Report

--------------------------

Student Name: {student_name}
Score: {score}
Status: {status}
Grade: {letter}"""
    return report

def save_report(student_name, report):
    filename = f"{student_name.lower().replace(' ', '_')}_report.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)
    return filename
    