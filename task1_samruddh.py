Code:
name = input("Enter your name: ")
age_str = input("Enter your age: ")
city = input("Enter your city: ")
favourite_subject = input("Enter your favourite subject: ")

age = int(age_str)

birth_year = 2024 - age

print("\n" + "="*30)
print(f"        PROFILE CARD        ")
print("="*30)
print(f"Name:              {name}")
print(f"Age:               {age}")
print(f"Estimated Birth:   {birth_year}")
print(f"City:              {city}")
print(f"Favourite Subject: {favourite_subject}")
print("="*30)


Output:
Enter your name: Samruddh Jadhav
Enter your age: 19
Enter your city: Mumbai
Enter your favourite subject: Data Structures

==============================
        PROFILE CARD        
==============================
Name:              Samruddh Jadhav
Age:               19
Estimated Birth:   2005
City:              Mumbai
Favourite Subject: Data Structures
==============================
