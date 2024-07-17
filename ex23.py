num = int(input("Informe um número: "))
n = 0
soma = 0
lista = []

while (n < num):
    n = n + 1

    if (num % n == 0 and n != 66):

        lista.append(n)

print(sum(lista))