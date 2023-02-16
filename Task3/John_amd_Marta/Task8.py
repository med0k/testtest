"""
8. Create 2 variables john, marta. Variables must be dictionaries with keys: full_name, age, salary, gender, friends,
 coordinates.
Structure requirements:
Full_name - full name
Age - age
Salary - salary
Gender - the gender of the person (use boolean)
Friends - list of friends from task 6
Coordinates - longitude and latitude from task 7

Print the key and value for john and martha to console: “key => value” where key is the key of the dictionary pair
 and value is the value of the dictionary pair.
*challenge:
Task from point 8. Instead of strings in the list of friends, there should be the same dictionaries as john and marta.
Create 2 friends each for John and Martha. Print John and Martha's fields to the console
"""


john = {
    'full_name': "Johnny Lebowski",
    'Age': 32,
    'Salary': 3200,
    'Gender': True,
    'Friends': ['Petya', 'Misha', 'Lesha', 'Max'],
    'Coordinates': (38.34049, -0.49957)
}

marta = {
    'full_name': "Marta Hanckok",
    'Age': 28,
    'Salary': 6500.5,
    'Gender': False,
    'Friends': ['Coco', 'Shanel', 'Versacci', 'Don Vito'],
    'Coordinates': (19.5749, 28.49957)
}

rick = {
    'full_name': "Rick Sanchez",
    'Age': 56,
    'Salary': 100500
}

print("Key value Marta: \n", marta.items(), "\nKey value John: \n", john.items())
