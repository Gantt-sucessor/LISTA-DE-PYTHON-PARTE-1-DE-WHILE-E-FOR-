n = int(input("Informe a qnt de notas: "))
notas = []
soma = 0


while True:
    for i in range(n):
        nota = float(input("Informe a nota: "))
        notas.append(nota)
        soma = soma + nota
        media = soma / n
    
    print(media)
    n = int(input("Informe a qnt de notas: "))
    
    if (nota < 0 or nota > 10):
        print("fim do programa")      
        break
    
    
