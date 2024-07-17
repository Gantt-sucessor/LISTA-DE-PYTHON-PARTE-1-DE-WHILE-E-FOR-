n = int(input("Informe um número: "))

if (n <= 0):
    print("Positivo porra!!")
else:
    for i in range(n,0-1,-1):
        print(i)