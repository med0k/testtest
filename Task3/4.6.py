"""
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
"""

ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

spli_st = ospf_route.replace("via", "").replace("[", "").replace("]", "").replace(",", "").split()

print(spli_st)
print("Prefix: ",  spli_st[0], "\nAD/Metric: ", spli_st[1], "\nNext-Hop: ", spli_st[2],
      "\nLast update: ", spli_st[3], "\nOutbound Interface: ", spli_st[2])
