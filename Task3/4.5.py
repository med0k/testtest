"""
Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2 (пересечение).
В данном случае, результатом должен быть такой список: ['1', '3', '8']
Записать итоговый список в переменную result. (именно эта переменная будет проверяться в тесте)
Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.
"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

spli1 = command1.split(" ")
mnojestvo1 = set(spli1[-1].split(","))

spli2 = command2.split(" ")
mnojestvo2 = set(spli2[-1].split(","))

result = list(mnojestvo1.intersection(mnojestvo2))
print(result)

