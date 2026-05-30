import random

def main():
    print("=== Industrial Production Counter System ===")
    
    # 1. Input: Gather base manufacturing metrics
    target_units = int(input("Enter total production target units: "))
    workers_per_shift = int(input("Enter number of workers per shift: "))
    defect_rate_pct = float(input("Enter expected defect rate percentage (e.g., 10 for 10%): "))
    
    # Convert percentage to a probability decimal scale between 0.0 and 1.0
    defect_probability = defect_rate_pct / 100.0
    
    # Cumulative tracking statistics across all shifts
    total_good_units_produced = 0
    total_defects_found = 0
    target_reached = False

    print("\n--- Starting Production Simulation ---")

    # 2. Simulate 3 shifts using outer loop
    for shift in range(1, 4):
        if target_reached:
            break
            
        print(f"\n>> Shift {shift} Active")
        
        # Track metrics specific to the current shift
        shift_good_units = 0
        shift_defects = 0
        
        # 2. Simulate 20 machine cycles per shift using inner loop
        for cycle in range(1, 21):
            # Check a quick check condition before running the cycle
            if total_good_units_produced >= target_units:
                target_reached = True
                # 4. Stop ALL production when total target is reached using break
                print(f"   [ALERT] Target of {target_units} reached during Shift {shift}, Cycle {cycle}! Shutting down assembly lines lines.")
                break
            
            # Simulate a machine manufacturing attempt
            # Determine if the item is broken or passes quality control checks
            is_defective = random.random() < defect_probability
            
            if is_defective:
                shift_defects += 1
                total_defects_found += 1
                # 3. Randomly mark items as defective — skip processing them using continue
                continue  
            
            # If it wasn't skipped by the continue keyword above, it's a good unit
            shift_good_units += 1
            total_good_units_produced += 1
            
        # 5. Track per-shift: items produced, defects, worker productivity
        # Productivity Metric = Good units produced / Number of workers in that shift
        worker_productivity = shift_good_units / workers_per_shift
        
        print(f"   Good Units Produced: {shift_good_units}")
        print(f"   Defects Detected:    {shift_defects}")
        print(f"   Worker Productivity: {worker_productivity:.2f} units/worker")

    # --- Final Summary Report ---
    print("\n" + "="*45)
    print("         FINAL PRODUCTION RUN REPORT         ")
    print("="*45)
    print(f"Target Units Set:         {target_units}")
    print(f"Total Good Units Made:    {total_good_units_produced}")
    print(f"Total Defective Units:    {total_defects_found}")
    print(f"Target Target Successfully Met?  {'YES' if total_good_units_produced >= target_units else 'NO (Ran out of shifts)'}")
    print("=============================================")

if __name__ == "__main__":
    main()

Output:
Scenario A: The Target is Reached Early
=== Industrial Production Counter System ===
Enter total production target units: 30
Enter number of workers per shift: 5
Enter expected defect rate percentage (e.g., 10 for 10%): 15

--- Starting Production Simulation ---

>> Shift 1 Active
   Good Units Produced: 15
   Defects Detected:    5
   Worker Productivity: 3.00 units/worker

>> Shift 2 Active
   [ALERT] Target of 30 reached during Shift 2, Cycle 18! Shutting down assembly lines lines.
   Good Units Produced: 15
   Defects Detected:    2
   Worker Productivity: 3.00 units/worker

=============================================
         FINAL PRODUCTION RUN REPORT         
=============================================
Target Units Set:         30
Total Good Units Made:    30
Total Defective Units:    7
Target Target Successfully Met?  YES
=============================================

Scenario B: Run Completes without Reaching a High Target
=== Industrial Production Counter System ===
Enter total production target units: 100
Enter number of workers per shift: 10
Enter expected defect rate percentage (e.g., 10 for 10%): 10

--- Starting Production Simulation ---

>> Shift 1 Active
   Good Units Produced: 18
   Defects Detected:    2
   Worker Productivity: 1.80 units/worker

>> Shift 2 Active
   Good Units Produced: 18
   Defects Detected:    2
   Worker Productivity: 1.80 units/worker

>> Shift 3 Active
   Good Units Produced: 17
   Defects Detected:    3
   Worker Productivity: 1.70 units/worker

=============================================
         FINAL PRODUCTION RUN REPORT         
=============================================
Target Units Set:         100
Total Good Units Made:    53
Total Defective Units:    7
Target Target Successfully Met?  NO (Ran out of shifts)
=============================================
