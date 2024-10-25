def f(x):
    return 2 * x - 1
def wb(x):
    if x < 0:
        return -x
    else:
        return x
a = -1
b = 4
E = 0.0001
if f(a) * f(b) <=0:
    while wb(a-b) >E:
        s = (a+b)/2
        if f(a)*f(s) <=0:
            b=s
        else:
            a=s
print(a)