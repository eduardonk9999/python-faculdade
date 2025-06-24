# SENHA É COMPOSTA PELA PALAVRA "LIBERDADE"
# seguida do fatorial dos minuto que a máquina estiver marcando no momento
# da digitação da senha (se a máquina estiver marcando 5 minutos, a senha será 
# LIBERDADE120).
# Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha
# necessária para desbloqueio.

# 1Minuto == 60 Segundos

senhaInit = "LIBERDADE"
minutos = int(input("Digite o minuto atual: "))
senhaUser = input("Digite a senha: ")
fatorial = 1

for i in range(1, minutos + 1):
    fatorial *= i
    senhaUserMaisFatorial = senhaUser.upper() + str(fatorial)
    senhaUserATUALIZADA = senhaInit + str(fatorial)
    if(senhaUserMaisFatorial == senhaUserATUALIZADA):
        print("Senha correta")
    else:
        print("Senha errada :( ")