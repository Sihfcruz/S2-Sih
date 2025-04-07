soma=0
quant=0
print("me diga os valores, e te direi a soma e a média de tais")
print("caso queira encerrar o programa digite um numero negativo")
while True:
    valor=float(input("digite o valor"))
if valor<0:
        print("encerrado")
        break
    soma=soma+valor
    quant=quant+1
print("a soma dos valores é de:",soma)
print("a média dos valores é de:",soma/quant)
