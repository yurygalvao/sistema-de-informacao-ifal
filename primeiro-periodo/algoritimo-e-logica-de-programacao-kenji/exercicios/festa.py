lista = 'Yury' 
nome = input('Qual seu nome?')
idade = int(input('Qual a sua idade?'))

if(lista == nome and idade >= 18):
    print('Você pode entrar')
elif(lista == nome and idade < 18):
    autorizacao = int(input('Você tem autorização? 1 ou 0'))
    if autorizacao == True:
        print('Você pode entrar')
    else:
        print('Você foi barrado')



