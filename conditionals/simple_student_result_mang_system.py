# Declaring Variables
# Getting Student Names
student_firstname = input("Enter Firstname: ")
student_lastname = input("Enter lastname: ")
student_fullname = f"{student_firstname} {student_lastname}"

# Getting score for subjects
math_score = int(input("Enter your Mathematics score "))
eng_score = int(input("Enter your English Language score: "))
comp_sci_score = int(input("Enter your Computer Science score: "))

#
total_score = None
avg_score = None
grade = None
remark = None
output = None

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
    total_score = math_score + eng_score + comp_sci_score
    avg_score = float(total_score/3)
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
    # Outputting the result
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
print(output)
