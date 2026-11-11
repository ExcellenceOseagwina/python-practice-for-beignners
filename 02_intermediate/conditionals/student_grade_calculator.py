# LESSON: Ordered conditions and grade bands
# The score is written into the program instead of typed by a user. Change it
# to see which result each choice gives. Python checks choices in order.
student_name = "Hunter Wise"
student_score = 67
student_grade = None
student_final_result = None

# Check that the score is from 0 to 100 before choosing a grade. `or` means
# either one of these checks can make the condition true.
if student_score < 0 or student_score > 100:
    student_grade = "??"
    student_remark = "Result Rejected!"
    student_final_result = f'''
    Name: {student_name}
    Scored: {student_score}
    Remark: {student_remark}'''
    
# Check the highest grade first. Since earlier checks have failed, this is a
# score from 70 to 100.
elif student_score >= 70:
    student_grade = "A"
    student_remark = "Excellent"
    student_final_result = f'''
Name: {student_name}
Scored: {student_score}
Remark: {student_remark}'''

elif student_score >= 60:
    student_grade = "B"
    student_remark = "Very Good"
    student_final_result = f'''
    Name: {student_name}
    Scored: {student_score}
    Grade: {student_grade}
    Remark: {student_remark}'''

elif student_score >= 50:
    student_grade = "C"
    student_remark = "Good"
    student_final_result = f'''
    Name: {student_name}
    Scored: {student_score}
    Grade: {student_grade}
    Remark: {student_remark}'''

elif student_score >= 45:
    student_grade = "D"
    student_remark = "Pass"
    student_final_result = f'''
    Name: {student_name}
    Scored: {student_score}
    Grade: {student_grade}
    Remark: {student_remark}'''

else:
    student_grade = "F"
    student_remark = "Failed"
    student_final_result = f'''
    Name: {student_name}
    Scored: {student_score}
    Grade: {student_grade}
    Remark: {student_remark}'''


# Print the report made by the matching choice above.
print(student_final_result)
