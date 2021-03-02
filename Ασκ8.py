import urllib.request
import json

def getKeys(lex):
    lin = []
    for key in lex.keys():
        lin.append(key)

    return lin

def price(symbolism, symbols_comp=["EUR"]):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}&e=CCCAGG'\
            .format(symbolism.upper(), ','.join(symbols_comp).upper())
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    data=json.loads(html)
    return data

file = input("Enter file location: ")
f1 = open(file,'r')
f1 = f1.read()
f1 = json.loads(f1)
z=getKeys(f1)
tmp={}
for i in z:
    tp1 = price(i)
    tp[i] = tp1["EUR"]*f1[i]
print('Your web-portofolio is: ')
print(f1)
print('Which in euros is: ')
print(tp)
