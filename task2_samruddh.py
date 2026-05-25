Code:
# 1. Inputs: Total bill, number of people, and tip percentage
total_bill = float(input("Enter the total bill amount: $"))
number_of_people = int(input("Enter the number of people splitting the bill: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

# 2 & 3. Calculations utilizing all arithmetic operators (+, -, *, /, %)

# Operator [*] and [/] to find the absolute tip amount
tip_amount = total_bill * (tip_percentage / 100)

# Operator [+] to find the final bill total
total_with_tip = total_bill + tip_amount

# Operator [/] to find how much each person owes
amount_per_person = total_with_tip / number_of_people

# Operator [%] to check for any uneven remaining cents after a split
remaining_cents = total_with_tip % number_of_people

# Operator [-] to show how much of the original bill was purely food/service before tax/tip
# (or just a fun metric like subtraction from a $1000 budget cap)
budget_leeway = 1000.0 - total_with_tip

# 4. Round results to 2 decimal places and print a neat summary
print("\n" + "="*40)
print("          BILL SPLIT SUMMARY          ")
print("="*40)
print(f"Original Bill:      ${round(total_bill, 2)}")
print(f"Tip Amount ({tip_percentage}%): ${round(tip_amount, 2)}")
print(f"Total with Tip:     ${round(total_with_tip, 2)}")
print(f"Number of People:   {number_of_people}")
print("-"*40)
print(f"EACH PERSON OWES:   ${round(amount_per_person, 2)}")
print("-"*40)
print(f"Uneven remainder:   ${round(remaining_cents, 2)} (leftover fractional cents)")
print(f"Remaining Budget:   ${round(budget_leeway, 2)} (from a $1000 limit)")
print("="*40)

Output:
Enter the total bill amount: $3000
Enter the number of people splitting the bill: 5
Enter the tip percentage (e.g., 15 for 15%): 10

========================================
          BILL SPLIT SUMMARY          
========================================
Original Bill:      $3000.0
Tip Amount (10.0%): $300.0
Total with Tip:     $3300.0
Number of People:   5
----------------------------------------
EACH PERSON OWES:   $660.0
----------------------------------------
Uneven remainder:   $0.0 (leftover fractional cents)
Remaining Budget:   $-2300.0 (from a $1000 limit)
========================================
