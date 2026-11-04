valor = int(input("Digite o valor da sua compra: "))

if valor < 250:
    print("Poxa, falta pouco para você ganhar um desconto de 10%")
elif valor >= 250 and valor < 500:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
else: 
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")