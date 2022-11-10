num = []
numMul2 = []
numMul3 = []
numMul2e3 = []

for n in range(0,7):
    num.append(int(input(f"Digite o {n + 1} número: ")))
    if num[n]% 2 == 0:
        numMul2.append(num[n])
    if num[n]% 3 == 0:
        numMul3.append(num[n])
    if num[n]% 3 ==0 and num[n]% 2 == 0:
        numMul2e3.append(num[n])
    
print(f"lista dos números digitados divisíveis por 2: {numMul2}")
print(f"lista dos números digitados divisíveis por 3: {numMul3}")
print(f"lista dos números digitados divisíveis por 2 e 3: {numMul2e3}")