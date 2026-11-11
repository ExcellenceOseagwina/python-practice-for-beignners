# LESSON: Percentage calculation and equal sharing
# Enter the bill, tip percent, and number of people, in that order. float()
# allows decimal amounts; int() is for a whole number of people. Enter valid
# numbers and a group size greater than zero for this example.
bill = float(input())
tip_percent = float(input())
# Divide the tip percent by 100, then multiply by the bill to get the tip.
tip_amount = (tip_percent / 100) * bill
bill_per = int(input())

total_amount = tip_amount + bill
# Divide the bill and tip total evenly among the people.
split_bill = total_amount / bill_per

# The f-string puts the calculated amounts into the receipt.
print(f'''
Bill Split Calculator
Total (including tip): ${total_amount}
Each person pays: ${split_bill}
''')
