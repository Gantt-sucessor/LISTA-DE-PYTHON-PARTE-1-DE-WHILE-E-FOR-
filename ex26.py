x = int(input("Informe a base: "))
y = int(input("Informe o expoente: "))

cont = 0 
resultado = 1

while cont < y:

    resultado = resultado * x
    cont = cont + 1

print(resultado)