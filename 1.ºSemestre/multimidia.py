print("Opcoes de assinatura: Basic, Sliver, Gold, Platinum")
assinatura = input("Digite sua assinatura ")
faturamento = float(input("Digite seu faturamento anual "))


if assinatura == "Basic":
    desconto = faturamento * (30 / 100)
   
    print("Seu desconto é: {}".format(desconto))
elif assinatura == "Sliver":
    desconto = faturamento * (20 / 100)
    print("Seu desconto é: {}".format(desconto))
elif assinatura == "Gold":
    desconto = faturamento * (10 / 100)
    print("Seu desconto é: {}".format(desconto))
elif assinatura == "Platinum":
    desconto = faturamento * (5 / 100)
    print("Seu desconto é: {}".format(desconto))
else:
    desconto = 0