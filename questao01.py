num: int
num = 6
numeros = []
ePar = 0
eImpar = 0

for n in range(0, num):
    numeros.append(int(input("Digite um número: ")))

for n in range(0, num):
    if numeros[n] % 2 == 0:
        print(numeros[n])
        ePar += 1
print(f"São números pares: {ePar}.")  

for n in range(0, num):
    if numeros[n] % 2 == 1:
        print(numeros[n])
        eImpar += 1
print(f"São números impares: {eImpar}. ")  

 
    
 