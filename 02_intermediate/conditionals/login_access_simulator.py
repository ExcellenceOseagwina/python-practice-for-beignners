# LESSON: Ask for a username and password, then decide
# This is a practice program with sample login details written in the file.
# Do not use this way of storing passwords in a real application.

# Save the username and password that this example will accept.
correct_username = "admin"
correct_password = "Cyber123"

# input() asks the user to type text. The program compares that text below.
username = input("Enter your username: ")
password = input("Enter your password: ")

# Start by saying access is False. Change it to True only when both details match.
access_granted = False
message = None

# First check whether the fields are empty and the username is correct. The
# inner if checks the password only when the username matches. '' means empty.
if username == '' or password == "":
    message = "Username and password cannot be empty."

elif username == correct_username:
    if password == correct_password:
        access_granted = True
        message = "Access granted!"
    else:
        message = "Incorrect password."

else: 
    message = "User not found."


# The f-string puts the username, access result, and message into this report.
print(f"""
==============================
       LOGIN RESULT
==============================
Username: {username}
Access Granted: {access_granted}
Message: {message}
==============================
""")
