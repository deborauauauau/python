produto1 = float(input("Informe o preço do primeiro produto: "))
produto2 = float(input("Informe o preço do segundo produto: "))
produto3 = float(input("Informe o preço do terceiro produto: "))

maior = produto1
menor = produto1

if produto2 > maior:
    maior = produto2
elif produto2 < menor:
    menor = produto2

if produto3 > maior:
    maior = produto3
elif produto3 < menor: 
    menor = produto3 



#Exibe o maior e o menor número número
print (f"O maior número é: {maior}")
print (f"O menor número é: {menor}")