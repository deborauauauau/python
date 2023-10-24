produto1 = float(input("Informe o preço do primeiro produto: "))
produto2 = float(input("Informe o preço do segundo produto: "))
produto3 = float(input("Informe o preço do terceiro produto: "))

if produto1 <= produto2 and produto1 <= produto3:
    menor_preco = produto1
elif produto2 <= produto3:
    menor_preco = produto2
else:
    menor_preco = produto3

#Exibe o maior número número
print (f"O menor número é: {menor_preco}")