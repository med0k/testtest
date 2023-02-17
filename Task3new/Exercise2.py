"""
2 There is a list of friends ["John", "Marta", "James", "Amanda", "Marianna"].
print to the console the names of each on a new line, right-aligned using the string method and formatting via f string.
Also, above the names, in the first line, display the headings Names where the word names should be in the middle,
and the rest of the space is filled with the symbol "*"
"""

list_friends = ["John", "Marta", "James", "Amanda", "Marianna"]
star = "Names"

print(f"**********{star}**********")
print(f"{list_friends[0]:>25}\n{list_friends[1]:>25}\n{list_friends[2]:>25}\n{list_friends[3]:>25}"
      f"\n{list_friends[4]:>25}")

