# Variables

# Variable For Top Design
top_design = '''
==================================================
                MY CYBER SECURITY PROFILE
==================================================

'''

# Worker's Detail Variables
worker_name = 'Excellence Oseobulu Oseagwina'
worker_age = 35
worker_country = 'Nigeria'

# Variable For Middle Design
middle_design = '''
--------------MY TECH STACK AND EXPERIENCE-------------

'''

# Worker's Stack Variables
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