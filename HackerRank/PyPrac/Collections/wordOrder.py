n=int(input());
from collections import OrderedDict;
itemnames=OrderedDict();
for i in range(n):
    item = input();
    itemnames[item] = itemnames.get(item, 0) + 1;
#for item, quantity in itemnames.items():
print(len(itemnames.keys()));
print (*itemnames.values());