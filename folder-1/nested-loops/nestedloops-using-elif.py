grades = [95, 72, 88, 65]
total_score = 0
for grade in grades:
    if grade >= 90:
        total_score += grade + 5  # Bonus for high grades
    else:
        total_score += grade
print("Total score:", total_score)




