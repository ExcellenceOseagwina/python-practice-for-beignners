username = input("Enter Username: ")
password = input("Enter Password: ")

access_granted = False
authenticated = False
user_role = None
requested_resource = None
message = None

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

if authenticated:
    requested_resource = input("Enter Requested Resource: ")
    if (
        requested_resource != "Dashboard"
        and requested_resource != "Security Reports"
        and requested_resource != "Security Configuration"
        and requested_resource != "Security Logs"
        and requested_resource != "User Management"
    ):
        message = "Invalid Requested Resource"
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
