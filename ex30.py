inicial = int(input("Informe o valor inicial do intervalo: "))
final = int(input("Informe o valor final do intervalo: "))
soma = 0
i = 0

if (inicial > final):
    print("Intervalo errado!")
else:
    for i in range(inicial,final):
        while (i % 2 != 0):
            soma = soma + i
            break

print(soma)