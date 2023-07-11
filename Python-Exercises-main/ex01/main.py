lista = [1, 2, 3 ,4 ,5]
print(lista)
lista.append(10)
print(lista)

#menor e maior numero
print(min(lista))
print(max(lista))

#Numeros impares e pares
listap = []
listai = []

for number in lista:
    if number % 2 == 0:
        listap.append(number)
    elif number % 2 != 0:
        listai.append(number)

print(listap)
print(listai)

#Contando elementos da lista
print(len(lista))

#revertendo a ordem
lista.reverse()
print(lista)

