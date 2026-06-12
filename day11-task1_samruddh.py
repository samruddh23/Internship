import csv

# 1. Create and Write to student.csv ---
# Defining 10 student records with 4 subjects each
# Schema: Roll No, Name, Math, Science, English, History
data = [
    ["Roll No", "Name", "Math", "Science", "English", "History"],
    [101, "Alice Smith", 85, 90, 78, 88],
    [102, "Bob Jones", 72, 65, 80, 70],
    [103, "Charlie Brown", 95, 92, 89, 94],
    [104, "Diana Prince", 88, 84, 91, 85],
    [105, "Evan Wright", 60, 72, 68, 74],
    [106, "Fiona Gallagher", 78, 81, 85, 80],
    [107, "George Clark", 91, 89, 94, 92],
    [108, "Hannah Abbott", 65, 70, 72, 68],
    [109, "Ian Malcolm", 83, 87, 79, 82],
    [110, "Julia Roberts", 90, 93, 88, 91]
]

filename = "student.csv"

# Writing data to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"'{filename}' created successfully with 10 student records.\n")


# 2. Read, Display, and Process the CSV Data ---
print("--- Student Records ---")

highest_score = -1
top_student = ""
total_marks_all_students = 0
total_subjects_counted = 0

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    # Print clean headers
    print(f"{header[0]:<10} {header[1]:<18} {header[2]:<6} {header[3]:<8} {header[4]:<8} {header[5]:<7} | Total")
    print("-" * 70)
    
    for row in reader:
        roll_no = row[0]
        name = row[1]
        # Convert marks from strings to integers
        marks = [int(m) for m in row[2:]]
        
        student_total = sum(marks)
        student_average = student_total / len(marks)
        
        # Display individual student row
        print(f"{roll_no:<10} {name:<18} {marks[0]:<6} {marks[1]:<8} {marks[2]:<8} {marks[3]:<7} | {student_total}")
        
        # Track the highest scorer based on total marks
        if student_total > highest_score:
            highest_score = student_total
            top_student = name
            
        # Accumulate marks for the global average calculation
        total_marks_all_students += student_total
        total_subjects_counted += len(marks)

print("-" * 70)


# 3. Display Highest Scorer and Overall Average ---
# Calculating overall average marks across all exams taken
overall_average = total_marks_all_students / total_subjects_counted

print(f"\nHighest Scorer: {top_student} with a total of {highest_score} marks.")
print(f"Average Marks of All Students (per subject): {overall_average:.2f}")


Output:
'student.csv' created successfully with 10 student records.

--- Student Records ---
Roll No    Name               Math   Science  English  History | Total
----------------------------------------------------------------------
101        Alice Smith        85     90       78       88      | 341
102        Bob Jones          72     65       80       70      | 287
103        Charlie Brown      95     92       89       94      | 370
104        Diana Prince       88     84       91       85      | 348
105        Evan Wright        60     72       68       74      | 274
106        Fiona Gallagher    78     81       85       80      | 324
107        George Clark       91     89       94       92      | 366
108        Hannah Abbott      65     70       72       68      | 275
109        Ian Malcolm        83     87       79       82      | 331
110        Julia Roberts      90     93       88       91      | 362
----------------------------------------------------------------------

Highest Scorer: Charlie Brown with a total of 370 marks.
Average Marks of All Students (per subject): 81.95
