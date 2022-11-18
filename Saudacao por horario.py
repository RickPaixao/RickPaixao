nome = input('Ola, digite seu nome: ')
print()
print(f'Ola {nome}, tudo bem?...')
h1 = input(f'{nome}, que hora são?: ')

if h1.isdigit():
    h1 = int(h1)
    if h1 < 0 or h1 > 23:
        print(f'{nome}, Digite um horario entre 0. Game e 23.')
    else:
        if    h1 <= 11:
            print(f'Bom Dia {nome}, ainda está cedo né')
        elif h1 <= 17:
            print(f'Boa Tarde {nome}, nossa já está de tarde')
        else:
           print(f'Boa Noite {nome}, Escureceu rápido hoje né?')
else:
    print(f'{nome}, acho que o que você digitou "{h1}" não é um horário valido.')
