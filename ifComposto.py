##variáveis
##    idade: inteiro
##    rm: alfanumérico
##início
##    Escreva “Por favor, digite seu RM”
##    Leia rm
##    Escreva “Por favor, digite sua idade”
##    Leia idade
##    Se idade >=18 então
##        Escreva “Sua participação foi autorizada, aluno de RM”, rm
##        Escreva “Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!”
##        Fim_se
##    Se idade <18 então
##        Escreva “Sua participação não foi autorizada por causa da sua idade”
##          Fim_se
##    Fim

rm = input("Insira seu RM: ")
idade = input("Sua idade: ")


if(idade >= 18):
    print("Sua participação foi autorizada, aluno de RM{}!".format(rm))
    print("Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!")

else:
    print("Sua participação não foi autorizada por causa da sua idade{}!".format(idade))
    if autorizado == 'S':
        print("Sua participação foi atutorizada, aluno de RM {}!".format(rm))
        print("Mais informções serão enviadas para o email responsável!")
    else:
        print("Sua participacao não foi autorizada por causa da sua idade")
