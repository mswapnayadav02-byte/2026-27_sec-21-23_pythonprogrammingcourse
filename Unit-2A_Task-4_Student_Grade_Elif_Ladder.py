##check student grade based on score
score = float(input("enter student's score:"))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print(f"student's grade is {grade}")