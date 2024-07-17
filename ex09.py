lista = []

for i in range(10):
    n = int(input("Informe 10 numeros: "))
    lista.append(n)

maior = max(lista)
menor = min(lista)
print("O maior elemento é: ",maior)
print("O menor elemento é: ",menor)