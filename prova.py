for _ in range(3):
    valor_compra = float(input("Digite o valor da compra: "))

if valor_compra <= 1500.00:
    percentual_desconto= 5
elif valor_compra <= 2000.00:
    percentual_desconto=10
elif valor_compra <= 3000.00:
    percentual_desconto = 15
else:
    percentual_desconto=20

desconto = (valor_compra * percentual_desconto)/100
valor_final = valor_compra - desconto

print(f"Valor da compra: {valor_compra:.2f}")
print(f"Percentual do desconto aplicado: {percentual_desconto}")
print (f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor a ser pago: R${valor_final:.2f}")

        
