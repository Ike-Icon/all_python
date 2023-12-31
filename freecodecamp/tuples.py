# Tuples & Dictionaries
d = dict()
d["csev"] = 2
d["cwen"] = 4

for k, v in d.items():
    print(k, v)

counts = 0
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)
