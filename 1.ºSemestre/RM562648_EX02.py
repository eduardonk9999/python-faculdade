preco = float(input("Digite o preço do carro:"))
print(f"O preço final à vista com desconto 20% é:{preco * 0.8}")

parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
juros = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

for i in range(len(parcelas)):
    acrescimo = preco * (juros[i] / 100)
    total = preco + acrescimo
    valor_parcela = total / parcelas[i]
    print(f"O preço final parcelado em {parcelas[i]} X é de R$ {total:.2f} com parcelas de R$ {valor_parcela:.2f}")