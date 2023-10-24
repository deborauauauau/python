#Solicita três números ao usuário.
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input ("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))
maior_numero= numero1
#Verifica qual é o maior número usando condicionais if-else

if numero1>=numero2 and numero1 >= numero3:         
    maior_numero=numero1
elif numero2 >= numero1>= numero3: 
    maior_numero =  numero2
else:
    maior_numero=numero3

    #Exibe o maior número                                                                                                                      
print (f"O maior número é: {maior_numero}")

