# Função para adicionar estudante
def adicionar_estudante(estudantes):
    nome = input("Digite o nome do estudante: ")
    if nome not in estudantes:
        estudantes[nome] = {'notas': {}, 'status': None}
        print(f"Estudante {nome} adicionado com sucesso.")
    else:
        print(f"Estudante {nome} já existe.")

# Função para adicionar notas do estudante
def adicionar_notas(estudantes):
    nome = input("Digite o nome do estudante: ")
    if nome in estudantes:
        print(f"Digite as notas do estudante {nome}:")
        try:
            matematica = float(input("Nota de Matemática (0-10): "))
            biologia = float(input("Nota de Biologia (0-10): "))
            portugues = float(input("Nota de Português (0-10): "))
            
            # Verificando se as notas são válidas (entre 0 e 10)
            if 0 <= matematica <= 10 and 0 <= biologia <= 10 and 0 <= portugues <= 10:
                estudantes[nome]['notas'] = {'matematica': matematica, 'biologia': biologia, 'portugues': portugues}
                
                # Calculando a média
                media = (matematica + biologia + portugues) / 3
                
                # Determinando aprovação ou reprovação
                if media >= 6:
                    estudantes[nome]['status'] = 'Aprovado'
                else:
                    estudantes[nome]['status'] = 'Reprovado'
                print(f"Notas de {nome} adicionadas com sucesso.")
            else:
                print("As notas devem estar entre 0 e 10.")
        except ValueError:
            print("Por favor, insira valores numéricos válidos para as notas.")
    else:
        print(f"Estudante {nome} não encontrado.")

# Função para verificar quantos estudantes estão aprovados e reprovados
def verificar_aprovacao(estudantes):
    aprovados = 0
    reprovados = 0
    for aluno, dados in estudantes.items():
        if dados['status'] == 'Aprovado':
            aprovados += 1
        elif dados['status'] == 'Reprovado':
            reprovados += 1
    print(f"Estudantes Aprovados: {aprovados}")
    print(f"Estudantes Reprovados: {reprovados}")

# Função para o menu
def menu():
    estudantes = {}
    
    while True:
        print("\nMenu:")
        print("1. Adicionar estudante")
        print("2. Adicionar notas de Matemática, Biologia e Português")
        print("3. Verificar quantos estudantes aprovados e reprovados")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1/2/3/4): ")
        
        if opcao == '1':
            adicionar_estudante(estudantes)
        elif opcao == '2':
            adicionar_notas(estudantes)
        elif opcao == '3':
            verificar_aprovacao(estudantes)
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamando a função menu para iniciar o programa
menu()

