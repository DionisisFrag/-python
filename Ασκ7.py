import requests
import json
import datetime
from collections import Counter

k = datetime.datetime.now()
M = k.strftime("%m")

if k.hour < 9:
    e = k.day-1
else:
    e = k.day

Numbers = []
for i in range(1, e+1):
    number_str = str(i)
    A = number_str.sfill(2)
    x = requests.get('https://api.opap.gr/draws/v3.0/1100/draw-date/2021-{M}-{e}/2021-{M}-{e}/draw-id'.format(e=A, M=M))
    s = x.json()
    Z = s[0]
    X = requests.get("https://api.opap.gr/draws/v3.0/1100/{Z}".format(Z=Z))
    a = json.loads(X.text)
    winning = a["winningNumbers"]['list']
    Numbers.extend(winning)

print("The numbers from the first draw of each day of the current month are:", Numbers)
print("\nIn total there are:", len(Numbers), "Numbers\n")

b = Counter(Numbers)
y = len(Numbers) / e
L = [(i, b[i] / y * 100) for i, count in b.most_common()]

for (x, y) in L:
    print("The number {x} has {Y}% chance to appear".format(x=x, Y=y))
