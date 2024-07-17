n = int(input("Informe quantos números serao informados: "))

for i in range(n):
    num = int(input("Fale o número: "))

    if(num % 2 == 0 and num != 0):
        print("É par")
    else:
        if (num == 0):
            print("fim programa")
            break

