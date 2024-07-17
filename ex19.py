num = int(input("Informe um número entre 100 e 9999: "))

if (num < 100 or num > 9999):
    print("Valor inválido")
else:
    final = str(num)

for i in final:
    print(i)