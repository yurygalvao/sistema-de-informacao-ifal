anuidade = int(input('Você está com a anuidade em dia? 1-Sim  0-Não'))
if anuidade == 1:
    print('Você pode entrar')
elif anuidade == 0:
    pagamento = int(input('Você precisa pagar 25 reais  1-Pago  0-Não pago'))
    if pagamento == 1:
        print('Você pode entrar')
    else:
        print("Você não pode entrar")
else:
    print('Você errou na digitação')