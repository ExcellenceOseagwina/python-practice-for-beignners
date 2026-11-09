# A Student Grade Calculator
# Declaring Variable
student_name = "Hunter Wise"
student_score = 67
student_grade = None
student_final_result = None

# Determining the final results of the student
if student_score < 0 or student_score > 100:
    student_grade = "??"
    student_remark = "Result Rejected!"
    student_final_result = f'''
    Name: {student_name}
    Scored: {student_score}
    Remark: {student_remark}'''
    
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


print(student_final_result)
