#Solicita três números ao usuário.
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input ("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))

#Verifica qual é o maior número sem usar 'and'
maior_numero = numero1

if numero2>numero1:         
    print (f"{numero2} é maior que {numero1} ")
if numero3 > maior_numero: 
    maior_numero =  numero3

    #Exibe o maior número                                                                                                                      
print (f"O maior número é: {maior_numero}")

