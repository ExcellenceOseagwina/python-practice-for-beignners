# Variables
customer_firstname = input("Enter Firstname: ")
customer_lastname = input("Enter Lastname: ")
customer_fullname = f"{customer_firstname} {customer_lastname}"

# Non-numeric input raises ValueError here.
unit_consumed = float(input("Enter Unit of Electricity Consumed: "))

rate_per_unit = None
total_bill = None
bill_message = None

# Check whether units_consumed is below 0.
if unit_consumed < 0:
    bill_message = f"""
Dear {customer_firstname}, you inputted {unit_consumed}. 
Try a unit from 0 or higher"""

else:
    if unit_consumed >= 0 and unit_consumed <= 100:
        rate_per_unit = 50
        electricity_bill = rate_per_unit * unit_consumed
        total_bill = electricity_bill
        bill_message = f"""
Name: {customer_fullname}
Rate Per Unit: {rate_per_unit}
Unit Consumed: {unit_consumed}
Total Bill Price: {total_bill}
"""
    
    elif unit_consumed > 100 and unit_consumed <= 200:
        rate_per_unit = 75
        electricity_bill = rate_per_unit * unit_consumed
        total_bill = electricity_bill
        bill_message = f"""
	Name: {customer_fullname}
	Rate Per Unit: {rate_per_unit}
	Unit Consumed: {unit_consumed}
	Total Bill Price: {total_bill}
	"""
    elif unit_consumed > 200:
        rate_per_unit = 100
        electricity_bill = rate_per_unit * unit_consumed
        total_bill = electricity_bill
        bill_message = f"""
Name: {customer_fullname}
Rate Per Unit: {rate_per_unit}
Unit Consumed: {unit_consumed}
Total Bill Price: {total_bill}
"""

# Display the result
print(bill_message)
