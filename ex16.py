n = int(input("Informe um número positivo: "))

if (n <= 0 or n % 2 == 0):
    print("Aprende pouco nengue")
else:
    for i in range(1,n+2,+2):
        print(i)