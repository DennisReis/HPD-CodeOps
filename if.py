score = int(input("Enter Score: "))
if score >= 80:
    grade = 'A'
else:
    if score >= 70:
        grade = 'B'
    else:
        grade = 'C'
print ("\n\nGrade is: %s" % grade)
