# Name: Aljade Bora
# Section: BSCS 1-1
# Program: Grade Calculator
# Description: Computes the midterm rating from three grades.

quiz_grade = 80
activities_grade = 75
exam_grade = 76

midterm_rating = (quiz_grade + activities_grade + exam_grade) / 3

print("Quiz grade:", quiz_grade)
print("Activities grade:", activities_grade)
print("Exam grade:", exam_grade)
print(f"Midterm rating: {midterm_rating:.2f}")