nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
comportamento = input('Digite o comportamento: B ou R')
media = (nota1 + nota2)/2
if media >= 6:
    print('Você foi aprovado!')
elif media >= 5 and comportamento == 'B':
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')