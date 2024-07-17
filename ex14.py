n = int(input("Informe um número positivo: "))

if (n <= 0 or n % 2 != 0):
    print("Valores inválidos baby")
else:
    for i in range(0,n+1,+2):
        print(i)