i = 100

while i >= 0:
    print(i)
    i -= 1


lista = []

for i in range (0, 101):
    lista.append(i)

print(sorted(lista, reverse=True))
