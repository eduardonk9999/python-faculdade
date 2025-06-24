consoleUm = "xbox"
consoleDois = "Playstation"
consoleTres = "Nintendo"

print("Escolha um número para votar no game. ")
print("Os Games são: 1: Xbox, 2: Playstation, 3: Nintendo ")

voto = float(input("Digite seu número: "))

if voto == 1:
    print("Você escolheu Xbox")
elif voto == 2:
    print("Você escolheu Playstation")
else:
    print("Você escolheu Nintendo")

