soma = 0
media = 0

for i in range(10):
    n = int(input("Informe um número: "))

    if (n > 0):
        soma = soma + n
        media = soma / 10       
    else:
        print("Informe apenas numeros positivos!")
        break

print("A media dos numeros ficou: ", media)
        

