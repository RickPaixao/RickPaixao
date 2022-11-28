print('Vamos brincar de Forca.')
print()
sct = input(f'Digite uma palavra chave: ').lower()
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print(f'Você perdeu!!!')
        break

    ltr = input(f'Digite uma letra: ')
    print()
    if ltr == sct:
        print(f'Boa!!!\nvocê acertou de uma vez só a palavra "{sct.title()}" de uma vez só')
        break
    elif len(ltr) > 1:
        print('Ops, apenas uma letra.')
        continue
    digitadas.append(ltr)

    if ltr in sct:
        print(f'Boa, tem a letra "{ltr.title()}"')

    else:
        print(f'Não tem a letra "{ltr.title()}"')
        digitadas.pop()

    sct1 = ''
    for ltr_crt in sct:
        if ltr_crt in digitadas:
            sct1 += ltr_crt
        else:
            sct1 += '*'
    print()
    if sct1 == sct:
        print(f'Boa você acertou a palavra "{sct.title()}"')
        break
    else:
        print(f'{sct1.title()}')

    if ltr not in sct1:
        chances -= 1

    print(f'Você ainta tem {chances} chances')
    print()
