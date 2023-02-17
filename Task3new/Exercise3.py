"""
3 There is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ". Convert this string to a dictionary
{name: Amanda, age: 32, salary: 1500, currency: euro}
"""

my_string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "

pairs = my_string.strip(' ').replace("&", " ").replace('=sssss', '').replace("=", " ").split(" ")
nw = pairs.pop(4)
my_dict = dict(zip(pairs[::2], pairs[1::2]))

print(my_dict)





