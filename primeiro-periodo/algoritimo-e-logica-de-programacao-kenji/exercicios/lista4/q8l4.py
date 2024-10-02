bf = int(input('Você possuiu bolsa família? 1-Sim  0-Não'))
filhos3 = int(input('Você possui mais de 3 filhos? 1-Sim  0-Não'))
if bf == 1 and filhos3 == 1:
    print('Você pode acessar a vaga de cotista')
else:
    print('Você não pode acessar a vaga de cotista')