"""
Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
„101010101010101010111011101110111100110011001100“
"""

mac = "AAAA:BBBB:CCCC"

new_mac = ''.join(format(ord(x), '08b') for x in mac)
print(new_mac)