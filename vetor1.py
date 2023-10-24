vetorA = [0] * 3
vetorB = [0] * 3
vetorC = [0] * 3
for i in range (3):
    vetorA[i]= int(input(f"Digite o valor da posição {i} do vetor A: "))
    vetorB[i]= int(input(f"Digite o valor da posição {i} do vetor B: "))
    vetorC[i]= int(input(f"Digite o valor da posição {i} do vetor C: "))
    vetorC [i] = vetorA [i] + vetorB [i]

   
print ('Vetor digitado:', vetorA)
print ('Vetor digitado:', vetorB)
print ('Vetor digitado:', vetorC)
print ("A soma do vetor A e do vetor B é: ",  )