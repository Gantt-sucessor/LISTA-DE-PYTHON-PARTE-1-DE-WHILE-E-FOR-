lista = []
qnt = int(input("Informe a quantidade de números que vai você vai querer ler: "))

for i in range(qnt):
    r = int(input("Escreva o numero: "))
    lista.append(r)

maior = max(lista)
print("Maior valor é: ",maior)