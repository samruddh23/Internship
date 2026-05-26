# Smart Temperature Advisor

print("=== Smart Temperature Advisor ===")

# 1. Input: Read the temperature in Celsius
# float() handles decimal temperatures (like 25.5°C) gracefully
temp = float(input("Enter the current temperature (°C): "))

print("\n--- Activity Advice ---")

# 2. Sequential range checking using an if-elif-else structure
if temp < 0:
    print("Advice: Freezing! Stay indoors and wear heavy clothing")

elif 0 <= temp <= 15:
    print("Advice: Cold. A jacket is recommended")

elif 16 <= temp <= 25:
    print("Advice: Pleasant weather! Great for outdoor activities")

elif 26 <= temp <= 35:
    print("Advice: Hot. Stay hydrated and use sunscreen")

else:  # This naturally catches everything above 35
    print("Advice: Extreme heat! Avoid going outside")

print("================================")


Output:
Test Case 1:
=== Smart Temperature Advisor ===
Enter the current temperature (°C): -7

--- Activity Advice ---
Advice: Freezing! Stay indoors and wear heavy clothing
================================

Test Case 2:
=== Smart Temperature Advisor ===
Enter the current temperature (°C): 23

--- Activity Advice ---
Advice: Pleasant weather! Great for outdoor activities
================================

Test Case 3:
=== Smart Temperature Advisor ===
Enter the current temperature (°C): 33

--- Activity Advice ---
Advice: Hot. Stay hydrated and use sunscreen
================================

Test Case 4:
=== Smart Temperature Advisor ===
Enter the current temperature (°C): 47

--- Activity Advice ---
Advice: Extreme heat! Avoid going outside
================================
