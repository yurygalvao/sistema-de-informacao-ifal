def adicionar_estudante(estudantes):
    nome = input('Digite o nome: ')
    if nome not in estudantes:
        estudantes[nome] = {'notas' : {}, 'status' : None}
        print(f'Estudante {nome} adicionado com sucesso!')
    else:
        print(f'Estudante {nome} já cadastrado')

def adicionar_notas(estudantes):
    nome = input('Digite o nome: ')
    if nome in estudantes:
        try:
            matematica = float(input('Nota de matemática: '))
            biologia = float(input('Nota de biologia: '))
            portugues = float(input('Nota de português: '))

            if 0 <= matematica <= 10 and 0 <= biologia <= 10 and 0 <= portugues <= 10:
                estudantes[nome]['notas'] = {'matematica' : matematica, 'biologia' : biologia, 'portugues' : portugues}

                if matematica >= 6 and biologia >= 6 and portugues >= 6:
                    estudantes[nome]['status'] = 'Aprovado'
                else:
                    estudantes[nome]['status'] = 'Reprovado'
            else:
                print('As notas devem estar entre 0 e 10.')
        except ValueError:
            print('Insira números válidos para as notas.')
    else:
        print(f'Estudante {nome} não encontrado.')

def verificar_aprovados(estudantes):
    aprovados = 0
    reprovados = 0
    for alunos, dados in estudantes.items():
        if dados['status'] == 'Aprovado':
            aprovados += 1
        else:
            reprovados += 1
    print(f'{aprovados} estudantes aprovados e {reprovados} estudantes reprovados')

def menu():
    estudantes = {}
    while True:
        print('\nMenu')
        print('1. Adicionar estudante')
        print('2. Adicionar notas')
        print('3. Aprovados e reprovados')
        print('4. Sair')
        try:
            opcao = int(input('Digite a opção (1/2/3/4): '))
            if opcao == 1:
                adicionar_estudante(estudantes)
            elif opcao == 2:
                adicionar_notas(estudantes)
            elif opcao == 3:
                verificar_aprovados(estudantes)
            elif opcao == 4:
                print('Saindo do programa...')
                break
            else:
                print('Opção inválida')
        except:
            print('Digite um número inteiro válido')

menu()