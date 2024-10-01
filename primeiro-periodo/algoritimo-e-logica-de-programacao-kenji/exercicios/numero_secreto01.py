numero_secreto = 8
chance = 0
print('Níveis de jogo')
print('Nível 1 - 7 chances')
print('Nível 2 - 5 chances')
print('Nível 3 - 3 chances')
nivel = int(input('escolha um nível:'))
if (nivel == 1):
    chance = 7
elif nivel == 2:
    chance = 5
elif nivel == 3:
    chance = 3
else:
    
chute = int(input('Digite seu chute: '))
if chute == numero_secreto: 
    print('Você acertou!')
elif chute > numero_secreto:
    print('O número secreto é menor')
elif chute < numero_secreto:
    print('O número secreto é maior')
else:
    print ('Você errou!')