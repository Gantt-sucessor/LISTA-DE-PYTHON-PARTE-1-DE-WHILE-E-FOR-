soma = 0
multi = 1
n1 = int(input("Informe o primeiro número inteiro: "))
n2 = int(input("Informe o segundo número inteiro: "))

for i in range(n1,n2+1):
    if (i % 2 == 0):
       soma = soma + i 
       soma2 = n1 + n2
       somafinal = soma + soma2
    else:
        multi = multi * i
        
print(somafinal)
print(multi)

