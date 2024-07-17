soma = 0
media = 0

for i in range(10):
    nota = float(input("Informe os numeros: "))
    soma = soma + nota
    media = soma / 10

print("A média ficou: ",media)