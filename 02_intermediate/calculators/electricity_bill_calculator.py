# LESSON: Tier selection with if/elif/else
# Collect text names and combine them into one full name with an f-string.
customer_firstname = input("Enter Firstname: ")
customer_lastname = input("Enter Lastname: ")
customer_fullname = f"{customer_firstname} {customer_lastname}"

# float() converts the typed unit quantity to a decimal-capable number.
# Non-numeric input raises ValueError here; this lesson assumes numeric input.
unit_consumed = float(input("Enter Unit of Electricity Consumed: "))

rate_per_unit = None
total_bill = None
bill_message = None

# Reject negative usage first. The choices below set a rate for each range of
# units used.
if unit_consumed < 0:
    bill_message = f"""
Dear {customer_firstname}, you inputted {unit_consumed}. 
Try a unit from 0 or higher"""

else:
    # For 0 through 100 units, use a rate of 50. `and` means both checks apply.
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
    
    # This choice covers more than 100 and up to 200 units.
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
    # Any amount over 200 units reaches this choice.
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

# Show the message for the customer's usage. The f-string adds the values.
print(bill_message)
