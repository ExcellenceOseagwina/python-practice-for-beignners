# LESSON GUIDE: Enter a bill amount, a tip percentage, and the number of people.
# The first two answers can include decimals; the group size is a whole number.
# The program turns the percentage into a fraction, adds the tip to the bill,
# divides by the group size, then places both results in an f-string receipt.
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
