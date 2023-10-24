vetorA =[]
vetorB = [0] * 3
vetorC = []

for _ in range (3):
    elemento = int(input(f"Digite o valor na posição {_}:"))
    vetorA.append (elemento)
for i in range (3):
    vetorB[i] = int(input(f"Digite o valor na posição {i}: "))

for i in range (len(vetorA)):
    vetorC.append (vetorA[i] + vetorB [i])

print ("Vetor C", vetorC)