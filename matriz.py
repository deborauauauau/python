matrizA = [[0,0], [0,0]]
vetor = []
for i in range(2):
     for j in range(2):
          elementoA = int(input(f"Digite o elemento para a matriz A [{i}][{j}]: "))
          matrizA [i][j]= elementoA
          if i == j:
             vetor.append (elementoA)  
print ("Matriz A")
for linha in matrizA:
    print (linha)
print ("Os valores da diagonal da matriz A: ", vetor)