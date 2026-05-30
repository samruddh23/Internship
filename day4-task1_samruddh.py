import math

def calculate_emi():
    """Assignment 1: EMI Calculator"""
    print("\n--- 🛠️ EMI Calculator ---")
    try:
        principal = float(input("Enter loan principal amount (P): "))
        annual_rate = float(input("Enter annual interest rate in % (R): "))
        tenure_years = float(input("Enter tenure duration in years (N): "))
        
        # Monthly interest conversion
        # Rate per month = Annual Rate / (12 months * 100 percentage factor)
        monthly_rate = annual_rate / (12 * 100)
        
        # Months conversion
        total_months = tenure_years * 12
        
        # Mathematical Formula processing: 
        # EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
        if monthly_rate > 0:
            compounding_factor = math.pow(1 + monthly_rate, total_months)
            monthly_payment = (principal * monthly_rate * compounding_factor) / (compounding_factor - 1)
        else:
            # Simple fallback calculation for an interest-free layout
            monthly_payment = principal / total_months
            
        total_repayment = monthly_payment * total_months
        total_interest = total_repayment - principal

        # Formatted Display Output
        print(f"\nMonthly EMI Installment: ₹{monthly_payment:,.2f}")
        print(f"Total Repayment Value:   ₹{total_repayment:,.2f}")
        print(f"Total Interest Payable:  ₹{total_interest:,.2f}")
        
    except ValueError:
        print("[Error] Please enter numeric values only.")

def calculate_tax():
    """Assignment 2: Slab-Based Tax Calculator (Current India Default Slabs)"""
    print("\n--- 🛠️ Tax Calculator ---")
    try:
        gross_income = float(input("Enter annual taxable income (₹): "))
        
        # Applying structural default standard deduction for salaried individuals
        standard_deduction = 75000.0
        taxable_income = max(0.0, gross_income - standard_deduction)
        
        print(f"Income after Standard Deduction (₹75,000): ₹{taxable_income:,.2f}")
        
        # Current progressive progressive tax slabs
        slabs = [
            (400000, 0.00),   # Up to 4 Lakhs: Nil
            (800000, 0.05),   # 4L to 8L: 5%
            (1200000, 0.10),  # 8L to 12L: 10%
            (1600000, 0.15),  # 12L to 16L: 15%
            (2000000, 0.20),  # 16L to 20L: 20%
            (2400000, 0.25),  # 20L to 24L: 25%
            (float('inf'), 0.30) # Above 24L: 30%
        ]
        
        total_base_tax = 0.0
        previous_limit = 0
        breakdown = []
        
        # Conditional branching logic evaluating slab tiers sequentially
        for limit, rate in slabs:
            if taxable_income > previous_limit:
                taxable_amount_in_slab = min(taxable_income, limit) - previous_limit
                tax_for_slab = taxable_amount_in_slab * rate
                total_base_tax += tax_for_slab
                
                if taxable_amount_in_slab > 0:
                    breakdown.append((f"₹{previous_limit//100000}L - {f'₹{limit//100000}L' if limit != float('inf') else 'Above'}", rate * 100, tax_for_slab))
                previous_limit = limit
            else:
                break
                
        # Applying Section 87A rebate (Zero tax liability up to ₹12 Lakhs income threshold)
        if taxable_income <= 1200000:
            rebate = total_base_tax
            final_tax_before_cess = total_base_tax - rebate
            rebate_applied = True
        else:
            final_tax_before_cess = total_base_tax
            rebate_applied = False
            
        # 4% Health and Education Cess calculation
        cess = final_tax_before_cess * 0.04
        net_tax_payable = final_tax_before_cess + cess

        # Display Breakdown
        print("\n--- Progressive Income Tax Breakdown ---")
        for slab_range, percentage, calculated_tax in breakdown:
            print(f" Slab {slab_range:<15} @ {percentage:>2.0f}% | Charged: ₹{calculated_tax:,.2f}")
            
        print("-" * 45)
        print(f"Base Total Slab Tax:     ₹{total_base_tax:,.2f}")
        if rebate_applied:
            print(f"Sec 87A Rebate Applied: -₹{total_base_tax:,.2f} (Income <= ₹12L)")
        print(f"Health & Education Cess:  ₹{cess:,.2f}")
        print(f"NET TAX PAYABLE:          ₹{net_tax_payable:,.2f}")
        
    except ValueError:
        print("[Error] Please enter a valid number for income amount.")

def calculate_attendance():
    """Assignment 3: Attendance Calculator"""
    print("\n--- 🛠️ Attendance Calculator ---")
    try:
        classes_attended = int(input("Enter number of classes attended: "))
        classes_total = int(input("Enter total number of classes conducted: "))
        target_pct = float(input("Enter target attendance percentage required (e.g., 75): "))
        
        if classes_total <= 0:
            print("[Error] Total conducted classes must be greater than zero.")
            return
            
        current_pct = (classes_attended / classes_total) * 100
        print(f"\nYour current attendance profile stands at: {current_pct:.2f}%")
        
        if current_pct >= target_pct:
            print(f"Status Status: Clearance Met ✅. You are safely above your target constraint.")
            # Calculate safety margin room (how many upcoming sessions can be missed)
            # Formula derivation: (Attended) / (Total + X) = Target/100
            max_missable = math.floor((classes_attended * 100 / target_pct) - classes_total)
            print(f"Safety Margin: You can miss up to {max_missable} upcoming classes without dropping below {target_pct}%.")
        else:
            print(f"Status Status: Deficit Flagged ❌. You are below the required threshold.")
            # Calculate missing target requirements sequentially
            # Formula derivation: (Attended + X) / (Total + X) = Target/100
            required_classes = math.ceil((target_pct * classes_total - 100 * classes_attended) / (100 - target_pct))
            print(f"Recovery Path: You must attend the next {required_classes} consecutive classes back-to-back to reach {target_pct}%.")
            
    except ValueError:
        print("[Error] Please input integer format metrics for counts.")

def main():
    while True:
        print("\n=========================================")
        print("    🧰 MINI PROJECT — UTILITY TOOLKIT    ")
        print("=========================================")
        print("1. Launch EMI Loan Calculator")
        print("2. Launch Slab-Based Income Tax Calculator")
        print("3. Launch Class Attendance Planner")
        print("4. Terminate Toolkit System")
        print("=========================================")
        
        choice = input("Select a utility module to execute (1-4): ").strip()
        
        if choice == '1':
            calculate_emi()
        elif choice == '2':
            calculate_tax()
        elif choice == '3':
            calculate_attendance()
        elif choice == '4':
            print("\nShutting down internal toolkit engines. Goodbye!")
            break
        else:
            print("\n[Invalid Selection] Please choose an alternative route from options 1 through 4.")

if __name__ == "__main__":
    main()

Output:
=========================================
    🧰 MINI PROJECT — UTILITY TOOLKIT    
=========================================
1. Launch EMI Loan Calculator
2. Launch Slab-Based Income Tax Calculator
3. Launch Class Attendance Planner
4. Terminate Toolkit System
=========================================
Select a utility module to execute (1-4): 1

--- 🛠️ EMI Calculator ---
Enter loan principal amount (P): 100000
Enter annual interest rate in % (R): 12
Enter tenure duration in years (N): 10

Monthly EMI Installment: ₹1,434.71
Total Repayment Value:   ₹172,165.14
Total Interest Payable:  ₹72,165.14

=========================================
    🧰 MINI PROJECT — UTILITY TOOLKIT    
=========================================
1. Launch EMI Loan Calculator
2. Launch Slab-Based Income Tax Calculator
3. Launch Class Attendance Planner
4. Terminate Toolkit System
=========================================
Select a utility module to execute (1-4): 2

--- 🛠️ Tax Calculator ---
Enter annual taxable income (₹): 3600000
Income after Standard Deduction (₹75,000): ₹3,525,000.00

--- Progressive Income Tax Breakdown ---
 Slab ₹0L - ₹4L       @  0% | Charged: ₹0.00
 Slab ₹4L - ₹8L       @  5% | Charged: ₹20,000.00
 Slab ₹8L - ₹12L      @ 10% | Charged: ₹40,000.00
 Slab ₹12L - ₹16L     @ 15% | Charged: ₹60,000.00
 Slab ₹16L - ₹20L     @ 20% | Charged: ₹80,000.00
 Slab ₹20L - ₹24L     @ 25% | Charged: ₹100,000.00
 Slab ₹24L - Above    @ 30% | Charged: ₹337,500.00
---------------------------------------------
Base Total Slab Tax:     ₹637,500.00
Health & Education Cess:  ₹25,500.00
NET TAX PAYABLE:          ₹663,000.00

=========================================
    🧰 MINI PROJECT — UTILITY TOOLKIT    
=========================================
1. Launch EMI Loan Calculator
2. Launch Slab-Based Income Tax Calculator
3. Launch Class Attendance Planner
4. Terminate Toolkit System
=========================================
Select a utility module to execute (1-4): 3

--- 🛠️ Attendance Calculator ---
Enter number of classes attended: 23
Enter total number of classes conducted: 30
Enter target attendance percentage required (e.g., 75): 60

Your current attendance profile stands at: 76.67%
Status Status: Clearance Met ✅. You are safely above your target constraint.
Safety Margin: You can miss up to 8 upcoming classes without dropping below 60.0%.

=========================================
    🧰 MINI PROJECT — UTILITY TOOLKIT    
=========================================
1. Launch EMI Loan Calculator
2. Launch Slab-Based Income Tax Calculator
3. Launch Class Attendance Planner
4. Terminate Toolkit System
=========================================
Select a utility module to execute (1-4): 4

Shutting down internal toolkit engines. Goodbye!
