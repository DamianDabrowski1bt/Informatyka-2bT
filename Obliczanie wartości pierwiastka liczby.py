def wb(x):
    if x < 0:
        return -x
    else:
        return x
P = int(input("Podaj liczbe: "))
a = 1
b = P
E = 0.0001
while wb(a - b) > E:
    a = (a + b) / 2
    b = P/a
print("a1:", a, "\na2", b)