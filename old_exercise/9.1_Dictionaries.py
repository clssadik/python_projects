student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for letter in student_scores:
    student_grades[letter] = student_scores[letter]
    if 91 <= student_scores[letter] <= 100:
        student_grades[letter] = "Outstanding"
    elif 81 <= student_scores[letter] <= 90:
        student_grades[letter] = "Exceeds Expectations"
    elif 71 <= student_scores[letter] <= 80:
        student_grades[letter] = "Acceptable"
    else:
        student_grades[letter] = "Fail"

for letter in student_grades:
    print(f"{letter}: {student_grades[letter]}")