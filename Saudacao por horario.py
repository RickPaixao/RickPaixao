import datetime

hora = datetime.datetime.now()
hora = str(hora)
hr = hora[11:13]

nome = input('Ola, digite seu nome: ')
print()
print(f'{nome}, Agora são {hora[11:16]}')

if hr.isdigit():
    hr = int(hr)
    if hr < 0 or hr > 23:
        print(f'{nome}, Digite um horario entre 0. Game e 23.')
    else:
        if    hr <= 11:
            print(f'Bom Dia {nome}, ainda está cedo né')
        elif hr <= 17:
            print(f'Boa Tarde {nome}, nossa já está de tarde')
        else:
           print(f'Boa Noite {nome}, Escureceu rápido hoje né?')
else:
    print(f'{nome}, acho que o que você digitou "{hr}" não é um horário valido.')