# Enhanced Loan Eligibility System

print("=== Loan Eligibility Portal ===")

# 1. Gather Inputs from the User
age = int(input("Enter applicant's age: "))
salary = float(input("Enter monthly salary (in ₹): "))
employment = input("Enter employment type (salaried / self-employed): ").strip().lower()

print("\n--- Processing Application ---")

# 2. Check Baseline Rules first
# Baseline constraints: Age 21-60, Salary >= 25000, Employment must be 'salaried' or 'self-employed'
if not (21 <= age <= 60):
    print("Status: Rejected")
    print("Reason: Age must be between 21 and 60 years.")

elif salary < 25000:
    print("Status: Rejected")
    print("Reason: Monthly salary must be at least ₹25,000.")

elif employment not in ['salaried', 'self-employed']:
    print("Status: Rejected")
    print("Reason: Invalid employment type. Must be 'salaried' or 'self-employed'.")

else:
    # 3. If baseline rules pass, check special condition flags
    
    # Flag A: Young age group with lower salary spectrum
    if 21 <= age <= 30 and salary < 30000:
        print("Status: Needs guarantor")
        print("Note: Application provisionally accepted pending a verified guarantor profile.")
        
    # Flag B: Senior age group running independent business operations
    elif age > 55 and employment == "self-employed":
        print("Status: High risk, senior review needed")
        print("Note: Routing file to senior underwriters for commercial credit review.")
        
    # Flag C: Clean pass through all criteria
    else:
        print("Status: Approved")
        print("Congratulations! Your loan profile meets all baseline clearance criteria.")

print("===============================")


Output:
Test Case 1:
=== Loan Eligibility Portal ===
Enter applicant's age: 29
Enter monthly salary (in ₹): 55000
Enter employment type (salaried / self-employed): salaried

--- Processing Application ---
Status: Approved
Congratulations! Your loan profile meets all baseline clearance criteria.
===============================

  Test Case 2:
=== Loan Eligibility Portal ===
Enter applicant's age: 24
Enter monthly salary (in ₹): 24500
Enter employment type (salaried / self-employed): self employed

--- Processing Application ---
Status: Rejected
Reason: Monthly salary must be at least ₹25,000.
===============================

Test Case 3:
=== Loan Eligibility Portal ===
Enter applicant's age: 56
Enter monthly salary (in ₹): 45000
Enter employment type (salaried / self-employed): self-employed

--- Processing Application ---
Status: High risk, senior review needed
Note: Routing file to senior underwriters for commercial credit review.
===============================


                                           
                                  
                                          
