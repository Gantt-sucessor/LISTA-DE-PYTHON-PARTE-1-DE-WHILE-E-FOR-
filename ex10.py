n = int(input("Informe um número: "))
cont = 0
numero = 1

while (cont < n):
    if (numero % 2 != 0):
        print(numero)
        cont = cont + 1
    numero = numero + 1

