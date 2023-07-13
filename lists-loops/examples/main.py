list = ["maça", "banana", "laranja", "uva", "melancia"]

for i, value in enumerate(list):
    print("início --------")
    print("index: ", i)
    # print("valor: ", list[i])
    print("valor: ", value)
    print("index do próximo: ", i+1)
    print("valor do próximo: ", list[i+1])
    print("valor do anterior: ", list[i-1])
    print("fim ----------")
    # ------
    prox = list[i+1]
    atual = value
    menor = 0

    if prox > atual:
        menor = atual

