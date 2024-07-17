n = int(input("Informe um número inteiro: "))
soma = 0

if (n <= 0):
    print("Nada")
else:
    for i in range(0,n+1):
        soma = soma + i

print(soma)

