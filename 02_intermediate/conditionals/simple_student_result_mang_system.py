# LESSON: Input, validation, averages, and nested grade decisions
# input() gives us text. Names stay as text, and int() changes each score into
# a whole number so we can add and compare the scores.
student_firstname = input("Enter Firstname: ")
student_lastname = input("Enter lastname: ")
student_fullname = f"{student_firstname} {student_lastname}"

# Each subject has its own score so we can check and show them separately.
math_score = int(input("Enter your Mathematics score "))
eng_score = int(input("Enter your English Language score: "))
comp_sci_score = int(input("Enter your Computer Science score: "))

# None means these values have not been set yet. Later, output will hold either
# an error message or the student's report.
total_score = None
avg_score = None
grade = None
remark = None
output = None

# Parentheses let this long check continue over several lines. `or` means any
# score outside the allowed range makes the whole check true.
if (
    math_score < 0
    or math_score > 100
    or eng_score < 0
    or eng_score > 100
    or comp_sci_score < 0
    or comp_sci_score > 100
):
    output = "Invalid Score. Try a valid score from 0 - 100"
else:
    # Add the scores and divide by 3 to find their average. :.2f shows the
    # average with two digits after the decimal point in the report.
    total_score = math_score + eng_score + comp_sci_score
    avg_score = float(total_score/3)
    # Check grades from highest to lowest. The first matching grade is used.
    if avg_score >= 70:
        grade = "A"
        remark = "Excellent Performance!"

    elif avg_score >= 60:
        grade = "B"
        remark = "Very Good Performance!"

    elif avg_score >= 50:
        grade = "C"
        remark = "Good Performance!"

    elif avg_score >= 45:
        grade = "D"
        remark = "Fair Performance!"

    elif avg_score >= 40:
        grade = "E"
        remark = "Pass!"

    else:
        grade = "F"
        remark = "Fail!"
    # Put the scores and results into a multiline report with an f-string.
    output = f'''
================================
       STUDENT RESULT REPORT
================================

Student Name: {student_fullname}

Mathematics:       {math_score}
English Language:  {eng_score}
Computer Science:  {comp_sci_score}

Total Score:       {total_score}/300
Average Score:     {avg_score:.2f}%
Grade:             {grade}
Remark:            {remark}

================================
'''
# Show the error message or the finished student report.
print(output)
