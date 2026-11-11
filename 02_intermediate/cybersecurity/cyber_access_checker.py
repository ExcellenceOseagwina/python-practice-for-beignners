# LESSON: Check a user's name, then check what they may open
# First the program checks the username and password. Then it checks which
# pages that user may open. These sample passwords are only for practice.
# input() gives us text, and the spelling and capital letters must match.
username = input("Enter Username: ")
password = input("Enter Password: ")

# Start with access denied. None means a value has not been chosen yet. The
# choices below set the role, requested page, and message.
access_granted = False
authenticated = False
user_role = None
requested_resource = None
message = None

# `and` means both the username and password must match. Each elif checks a
# different account.
if username == "admin" and password == "Admin123":
    authenticated = True
    user_role = "Admin"
elif username == "analyst" and password == "Analyst123":
    authenticated = True
    user_role = "Analyst"
elif username == "guest" and password == "Guest123":
    authenticated = True
    user_role = "Guest"
else:
    authenticated = False
    access_granted = False
    message = "Incorrect Username or Password or empty input field. Try again"

# Ask for a page only after the username and password match. First check that
# the page exists, then check whether that role may open it.
if authenticated:
    requested_resource = input("Enter Requested Resource: ")
    # If the requested page does not match any name in this list, it is invalid.
    if (
        requested_resource != "Dashboard"
        and requested_resource != "Security Reports"
        and requested_resource != "Security Configuration"
        and requested_resource != "Security Logs"
        and requested_resource != "User Management"
    ):
        message = "Invalid Requested Resource"
    # Admins may open every listed page. Analysts and guests have fewer choices.
    elif user_role == "Admin":
        access_granted = True
        message = "Access Granted! Authorization successful."
    elif user_role == "Analyst":
        if (
            requested_resource == "Dashboard"
            or requested_resource == "Security Reports"
            or requested_resource == "Security Logs"
        ):
            access_granted = True
            message = "Access Granted! Authorization successful."
        else:
            message = "Access Denied! invalid resource requests."

    elif user_role == "Guest":
        if requested_resource == "Dashboard":
            access_granted = True
            message = "Access Granted! Authorization successful."
        else:
            message = "Access Denied! invalid resource requests."

# Show asterisks in place of the password. The short if/else inside the f-string
# displays GRANTED or DENIED.
if authenticated:
    print(f"""
================================
     CYBERSECURITY ACCESS CHECKER
================================

Username: {username}
Password: ********

Role: {user_role}
Requested Resource: {requested_resource}

Access Status: {"GRANTED" if access_granted else "DENIED"}
Authorization: {message}

================================
""")
else:
    print(message)
