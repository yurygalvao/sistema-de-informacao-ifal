for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))

    if(i==0):
        maiorNumero = num
        menorNumero = num
    if num > maiorNumero:
        maiorNumero = num
    if num < menorNumero:
        menorNumero = num

print("O maior número é:", maiorNumero)
print("O menor número é:", menorNumero)