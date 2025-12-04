import random
escreva = print
n1 = int(input('Digite um número de 1 a 10:'))
num = random.randint(1, 10)

if n1 == num:
    escreva("Acertou")

else:
    escreva(f"Errou. o Número correto foi {num} ")
