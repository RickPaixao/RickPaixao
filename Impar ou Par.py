'''
Faça uma programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro.
'''


nome = input('Digite seu nome: ')
print()
print(f'Ola {nome}, tudo bem?...')
n1 = input(f'{nome}, digite um numero: ')

if not n1.isdigit():
    print(f'O caractere "{n1}" não é um numero inteiro')
else:
    n1 = int(n1)
    if n1%2 == 1:
        print(f"O numero {n1} é Ímpar")

    elif n1%2 == 0:
        print(f"O numero {n1} é Par")