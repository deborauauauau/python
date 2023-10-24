
soma_peso=0
media_peso= 0
maior_100=0
for _ in range(10):
    peso = float(input("Informe seu peso: "))
    altura= float(input("Informe sua altura: "))
    soma_peso= soma_peso+peso

    if peso>=100 and altura<1.70:
        maior_100=maior_100+1

media_peso= soma_peso/5

print(f"Pessoas com mais de 100 quilos: {maior_100}") 
print(f"A média de peso entre as pessoas é: {media_peso:.1f }")

        
