print('Qual produto você deseja')
print('Banana - 1')
print('Mamão - 2')
print('Laranja - 3')
print('Goiaba - 4')
produto = int(input('Qual produto você deseja? 1 ou 2 ou 3 ou 4'))
if produto == 1:
    print('A banana custa 5 reais')
    preço = 5
elif produto == 2:
    print('O mamão custa 3 reais')
    preço = 3
elif produto == 3:
    print('A laranja custa 6 reais')
    preço = 6
elif produto == 4:
    print('A goiaba custa 2 reais')
    preço = 2
else:
    print('Produto inválido')

dinheiro = int(input('Me dê o dinheiro: '))
if dinheiro == preço:
    print('Tudo certo, volte sempre!')
else:
    print('Só aceitamos pagamento à vista')