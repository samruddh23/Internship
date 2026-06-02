print("=========================================================")
# #####################################################################
# # BUG 1 – RUNTIME ERROR DEMONSTRATION
# # Type  : IndexError
# # Cause : The loop attempts to iterate up to range(0, 6), but the array 
# #         list contains only 5 elements (indices 0 to 4).
# # Fix   : Iterate dynamically using range(len(marks)).
# #####################################################################
print("STAGE 1: Simulating Bug 1 (Runtime Error)...")

try:
    simulated_marks = [85, 92, 78, 90, 88]
    total = 0
    # Forcing index out-of-bounds loop intentionally
    for i in range(0, 6):
        total += simulated_marks[i]
except IndexError as e:
    print(f"💥 [Runtime Error Caught Successfully!]")
    print(f"   Error Type: {type(e).__name__}")
    print(f"   Message:    {e}")


print("\n" + "="*57)
# #####################################################################
# # BUG 2 – LOGICAL ERROR DEMONSTRATION
# # Type  : Algorithmic Logic Flaw
# # Cause : Initializing 'lowest_marks' to 0 ensures it remains 0, 
# #         as no real student mark will be less than 0.
# # Fix   : Initialize trackers using the first element of the dataset.
# #####################################################################
print("STAGE 2: Simulating Bug 2 (Logical Error)...")

simulated_marks = [85, 92, 78, 90, 88]
highest_marks = 0
lowest_marks = 0  # Flawed baseline setup

for score in simulated_marks:
    if score > highest_marks:
        highest_marks = score
    if score < lowest_marks:
        lowest_marks = score

print("⚠️ [Logical Error Run Finished Without Crashing]")
print(f"   Calculated Lowest Mark: {lowest_marks}  <-- (Wrong! Expected: 78)")


print("\n" + "="*57)
# =====================================================================
# # FIXED CODE: Production Ready Implementation
# =====================================================================
print("STAGE 3: Running Fixed & Clean Production Code...")

def run_clean_analytics():
    # Statically defining the 5 student marks for demonstration continuity
    production_marks = [85.5, 92.0, 78.0, 90.5, 88.0]
    print(f"Processing student marks dataset: {production_marks}")
    
    # 1. Total Marks safely calculated via correct loop boundaries
    total_marks = 0
    for i in range(len(production_marks)):  # FIXED: Runtime constraint bug resolved
        total_marks += production_marks[i]
        
    # 2. Average Marks
    average_marks = total_marks / len(production_marks)
    
    # 3 & 4. Highest and Lowest Marks safely tracked
    highest_marks = production_marks[0]  # FIXED: Initialized to real dataset element
    lowest_marks = production_marks[0]   # FIXED: Initialized to real dataset element
    
    for score in production_marks:
        if score > highest_marks:
            highest_marks = score
        if score < lowest_marks:
            lowest_marks = score

    # Clean Output Display Block
    print("\n-----------------------------------------")
    print("            METRICS REPORT               ")
    print("-----------------------------------------")
    print(f" 1. Total Marks:     {total_marks:.2f}")
    print(f" 2. Average Marks:   {average_marks:.2f}")
    print(f" 3. Highest Marks:   {highest_marks:.2f}")
    print(f" 4. Lowest Marks:    {lowest_marks:.2f}")
    print("=========================================================")

run_clean_analytics()

Output:
=========================================================
STAGE 1: Simulating Bug 1 (Runtime Error)...
💥 [Runtime Error Caught Successfully!]
   Error Type: IndexError
   Message:    list index out of range

=========================================================
STAGE 2: Simulating Bug 2 (Logical Error)...
⚠️ [Logical Error Run Finished Without Crashing]
   Calculated Lowest Mark: 0  <-- (Wrong! Expected: 78)

=========================================================
STAGE 3: Running Fixed & Clean Production Code...
Processing student marks dataset: [85.5, 92.0, 78.0, 90.5, 88.0]

-----------------------------------------
            METRICS REPORT               
-----------------------------------------
 1. Total Marks:     434.00
 2. Average Marks:   86.80
 3. Highest Marks:   92.00
 4. Lowest Marks:    78.00
=========================================================
