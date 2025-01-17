#zad 60.1
lista = []
ilosc = 0
x = 0
y = 0
with open("liczby.txt", "r") as plik:
    for i in plik:
        liczba = int(i)
        if liczba < 1000:
            ilosc +=1
            x = y
            y = liczba
            lista.append(liczba)
print(f"ilośc: {ilosc}")
print(f"Ostatnie 2 liczby poniżej 1000: {x},{y}")


#zad 60.2
for liczba in lista:
    lista2 = []
    for o in range(1,int(liczba**0.5)):
        if liczba % o == 0:
            lista2.append(o)
            lista2.append(liczba//o)
    if liczba % liczba**0.5 == 0:
        lista2.append(liczba**0.5)
    if len(lista2) == 18:
        lista2.sort()
        print(liczba,lista2)

#zad 60.3
najwieksza = max(lista)
wynik = None

for liczba in lista:
    wzgl_pierwsza = True
    for inna in lista:
        if liczba != inna:
            a, b = liczba, inna
            while b:
                a, b = b, a % b
            if a != 1:
                wzgl_pierwsza = False
                break
    if wzgl_pierwsza:
        wynik = liczba
        break

print("Największa liczba:", wynik)