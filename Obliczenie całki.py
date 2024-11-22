a = 0
b = 2
E = 10000
szerokosc = (b-a)/E
całka = 0

def f(x):
    return x*x +1


for i in range(E):
    wysokosc = f(a+i*szerokosc)
    całka += szerokosc * wysokosc
print(całka)


