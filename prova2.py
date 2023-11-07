vA = []
vB = []
vC = []
vD = []
vE = []

for i in range(5):
    elemento=float(input("Digite um elemento para o vetor A: "))
    vA.append(elemento)
    elemento=float(input("Digite um  elemento para o vetor B: "))
    vB.append(elemento)
    vC.append(vA[i] - vB[i])
    vD.append(vA[i] - vB[i])
    vE.append(vA[i] - vB[i])

print(f"O primeiro vetor informado foi ", vA)
print (f"O segundo vetor informado foi ", vB)
print(f"A diferença entre os vetores é: ", vC)
print(f"A soma entre os vetores é: ", vD)
print(f"A multiplicação entre os vetores é: ", vE)