lista = []

for i in range(1000000000):
    idade = int(input("Informe sua idade: "))
    lista.append(idade)

    if (idade == 0):
        soma = sum(lista)
        media = soma / (len(lista) - 1)
        break

print(media)