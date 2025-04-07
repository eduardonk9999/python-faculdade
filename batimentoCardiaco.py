# Até 2 anos - BPM A 140
# De 8 anos até 17 anos - 80 a 100
# Adulto sedentário 18 até 45 - 70 a 80
# idosos 45 até 90 - 50 a 60

#   elif 8 <= idade <= 17:

BPM = float(input("Iforme sue BPM: "))
IDADE = float(input("Informe sua idade: "))

if IDADE <= 2:
    print("BPM ATÉ 140")
elif 8 <= IDADE <= 17:
    print("BPM DE 80 a 100")
elif 18 <= IDADE <= 45:
    print("BPM entre 70 a 80, voce está sedentario ")
elif 45 < IDADE <= 90:
    print("IDOSO")
else:
    print("idade fora da faixa analisada")


