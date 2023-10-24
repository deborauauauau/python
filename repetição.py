
maior_18 = 0
soma_idade=0
media_idade = 0
for _ in range(5):
    idade = int(input("Informe sua idade:"))
    
    soma_idade = soma_idade + idade

    if idade >= 18:
        maior_18 = maior_18+1 
 
media = soma_idade/5

print(f"Pessoas com mais de 18 anos: {maior_18}") 
print(f"A média de idade entre as pessoas é: {media}")

