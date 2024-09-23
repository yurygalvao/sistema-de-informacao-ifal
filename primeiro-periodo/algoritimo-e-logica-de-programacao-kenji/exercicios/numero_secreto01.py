numero_secreto = 8
chute = int(input('Digite seu chute: '))
if chute == numero_secreto: 
    print('Você acertou!')
elif chute > numero_secreto:
    print('O número secreto é menor')
elif chute < numero_secreto:
    print('O número secreto é maior')
else:
    print ('Você errou!')
          


    

        