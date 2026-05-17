def is_valid_score(score):
    return 0 <= score <= 100

def classify_score(score):
    if score > 85:
        return "Excellent"
    elif score > 50:
        return "Passed"
    else: 
        return "Failed"

def grade_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    