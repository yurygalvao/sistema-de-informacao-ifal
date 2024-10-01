numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
numero4 = int(input('Digite o quarto número: '))
numero5 = int(input('Digite o quinto número: '))
maiorNumero = 1
menorNumero = 0

if (numero1 > numero2 and numero1 > numero3 and numero1 > numero4 and numero1 > numero5):
    maiorNumero = numero1
elif (numero2 > numero3 and numero2 > numero4 and numero2 > numero5):
    maiorNumero = numero2
elif( numero3 > numero4 and numero3 > numero5):
    maiorNumero = numero3
elif(numero4 > numero5):
    maiorNumero = numero4
else:
    maiorNumero = numero5

if (numero1 < numero2 and numero1 < numero3 and numero1 < numero4 and numero1 < numero5):
    menorNumero = numero1
elif (numero2 < numero3 and numero2 < numero4 and numero2 < numero5):
    menorNumero = numero2
elif( numero3 < numero4 and numero3 < numero5):
    menorNumero = numero3
elif(numero4 < numero5):
    menorNumero = numero4
else:
    menorNumero = numero5

print(f'{maiorNumero} é o maior número')
print(f'{menorNumero} é o menor número')
