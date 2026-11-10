# Declaring personal information variables
name = "Excellence Oseobulu Oseagwina"
country = "Nigeria"
degree = "B.Sc. Cyber Security"
age = 43
height = 1.64

# Declaring programming information variables
main_language = "Python"
learning_python = True
interested_in_cybersecurity = True

# Calculating next age
age_next_year = age + 1

if learning_python:
    status = "Currently learning Python!"

# Displaying the cybersecurity profile
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
