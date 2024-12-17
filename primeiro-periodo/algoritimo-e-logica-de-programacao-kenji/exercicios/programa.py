def adicionar_estudante(estudantes):
    nome = input('Digite o nome do estudante: ')
    if nome not in estudantes:
        estudantes[nome] = {'notas' : {}, 'status' : None}
        print(f'{nome} adicionado com sucesso.')
    else:
        print(f'{nome} já existe')


def adicionar_notas(estudantes):
    nome = input('Digite o nome: ')
    if nome in estudantes:
        print(f'Digite as notas do {nome}')
        try:
            matematica = float(input('Nota de matemática:(0-10) '))
            biologia = float(input('Nota de biologia:(0-10)' ))
            portugues = float(input('Nota de português:(0-10) '))
            

            if 0 <= matematica <= 10 and 0 <= biologia <= 10 and 0 <= portugues <= 10:
                estudantes[nome]['notas'] = {'matematica': matematica, 'biologia' : biologia, 'portugues' : portugues }

                media = (matematica + biologia + portugues)/3

                if media >= 6:
                    estudantes[nome]['status'] = 'Aprovado'
                else:
                    estudantes[nome]['status'] = 'Reprovado'
                print(f'Notas do {nome} adicionadas com sucesso')
            else:
                print('As notas devem estar entre 0 e 10.')
        except ValueError:
            print('Insira números válidos para as notas')
    else:
        print(f'Estudante {nome} não encontrado.')


def verificar_aprovacao(estudantes):
    aprovados = 0
    reprovados = 0
    for alunos, dados in estudantes.items():
        if dados['status'] == 'Aprovado':
            aprovados +=1
        else:
            reprovados +=1
    print(f'{aprovados} estudantes aprovados e {reprovados} reprovados')


def menu():
    estudantes = {}
    while True:
        print('Menu')
        print('1. Adicionar estudante')
        print('2. Adicionar notas de matemática, biologia e português.')
        print('3. Verificar quantos estudantes foram aprovados e reprovados')
        print('4. Sair')

        opcao = input('Digite a opção: (1/2/3/4) ')
        if opcao == '1':
            adicionar_estudante(estudantes)
        elif opcao == '2':
            adicionar_notas(estudantes)
        elif opcao == '3':
            verificar_aprovacao(estudantes)
        elif opcao == '4':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')

menu()