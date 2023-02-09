"""Преобразовать строку в переменной mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX Полученную новую строку
вывести на стандартный поток вывода (stdout) с помощью print.
"""

mac = "AAAA:BBBB:CCCC"
new_string = mac.replace(":", ".")

print(new_string)