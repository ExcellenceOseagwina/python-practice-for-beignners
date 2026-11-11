# LESSON: Different kinds of values and making a choice
# Strings are text, integers are whole numbers, floats have decimal points,
# and Booleans can only be True or False.
name = "Excellence Oseobulu Oseagwina"
country = "Nigeria"
degree = "B.Sc. Cyber Security"
age = 43
height = 1.64

# These True/False values represent yes-or-no facts.
main_language = "Python"
learning_python = True
interested_in_cybersecurity = True

# Add 1 to the current age. The value in age stays the same.
age_next_year = age + 1

# The if checks whether learning_python is True. The else handles False, so
# status gets a value either way.
if learning_python:
    status = "Currently learning Python!"

# The f-string puts the variable values into the profile text.
else:
    status = 'Not Learning Python'

print(f"""
========================================
       CYBERSECURITY PROFILE
========================================

Name: {name}
Country: {country}
Degree: {degree}
Age: {age}
Height: {height}m

Most Used Language: {main_language}
Learning Python: {learning_python}
Interested in Cybersecurity: {interested_in_cybersecurity}

Status: {status}
Age Next Year: {age_next_year}

========================================
""")
