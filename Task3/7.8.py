"""Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный поток вывода вывод столбцами,
таким образом:
- первой строкой должны идти десятичные значения байтов
-второй строкой двоичные значения
-Вывод должен быть упорядочен также, как в примере:
-столбцами
-ширина столбца 10 символов (в двоичном формате надо добавить два пробела между столбцами для разделения октетов между собой)
-Пример вывода для адреса 10.1.1.1:
"""

ip = "192.168.3.1"

a = ip.split(".")
ssd = "{:<10} {:<10} {:<10} {:<10}".format(a[0], a[1], a[2], a[3])
# need to add 1 more resul using format for второй строкой двоичные значения. Want to use 2 variants
print(ssd)

print(f"{a[0]:<10} {a[1]:<10} {a[2]:<10} {a[3]:<10}")
print(f"{bin(int(a[0])):<10} {bin(int(a[0])):<10} {bin(int(a[0])):<10} {bin(int(a[0])):<10}")


