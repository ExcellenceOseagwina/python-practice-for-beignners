# Login Access Simulator

# Declaring variables
correct_username = "admin"
correct_password = "Cyber123"

# Collecting user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Declaring the access status                          
access_granted = False
message = None

# Validate the login
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


# Display the result
print(f"""
==============================
       LOGIN RESULT
==============================
Username: {username}
Access Granted: {access_granted}
Message: {message}
==============================
""")