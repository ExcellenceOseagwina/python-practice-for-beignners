bill = float(input())
tip_percent = float(input())
tip_amount = (tip_percent / 100) * bill
bill_per = int(input())

total_amount = tip_amount + bill
split_bill = total_amount / bill_per

print(f'''
Bill Split Calculator
Total (including tip): ${total_amount}
Each person pays: ${split_bill}
''')