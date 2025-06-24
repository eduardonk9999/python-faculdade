import math

#solicitando os valores de A, B, C
a = float(input("Informe o valor de A"))
b = float(input("Informe o valor de B"))
c = float(input("Informe o valor de C"))

#cálculo de delta
delta = b * b - 4 * a * c

# verificação das condições com if encadeado

if delta > 0.0:
    # cálculo de 2 valores para X
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - match.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: 1x = {} e x2 = {}".format(a, b, c, x1, x2))
else:
    if delta == 0:
        # cálculo de 1 valor para x
        x = (-b + math.sqrt(delta)) / (2 * a)
        print("Para a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor: x = {}".format(a, b, c, x))
    else:
        # exibição de mensagem
        print("Para a equação {}x² + {}x + {} = 0, não valores reais para x".format(a, b, c))
                