# LESSON: Variables and calculated values
# The program stores profile data, reuses those values in calculations, then
# prints a report. Assignment (=) stores a value; it does not mean equality.

# Variable For Top Design
top_design = '''
==================================================
                MY CYBER SECURITY PROFILE
==================================================

'''

# These are examples of string and integer values. Variable names use
# underscores to make multiword names readable (a common Python convention).
worker_name = 'Excellence Oseobulu Oseagwina'
worker_age = 35
worker_country = 'Nigeria'

# Variable For Middle Design
middle_design = '''
--------------MY TECH STACK AND EXPERIENCE-------------

'''

# Expressions on the right are calculated before assignment: subtraction
# finds the age at the start of the experience period; multiplication converts
# years of experience to months. The original variables are not changed.
worker_degree = 'B.s.c Cyber Security'
worker_area_of_specialization = "Ethical Hacking"
worker_programming_language = 'Python'
worker_operating_system = 'Kali Linux'
worker_experience = 4
age_of_worker_during_year_1 = worker_age - worker_experience
months_of_learning = 12 * worker_experience

# Variable For Bottom Design
bottom_design = '''
=================================================
'''

# Print Out Data

# Worker's Details
print(top_design)

print("Name:", worker_name)
print("Age:", worker_age)
print("Country:", worker_country)

# Workers Stack
print(middle_design)

print("Degree:", worker_degree)
print("Area Of Expertize:", worker_area_of_specialization)
print("Programming Language:", worker_programming_language)
print("Operating System:", worker_operating_system)
print("Experience:", str(worker_experience) + " Years")
print("Age Of Worker During Year 1:", age_of_worker_during_year_1)
print("Months Spent For Learning:", months_of_learning, "Months")

print(bottom_design)
