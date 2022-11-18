c = 0
while True:
    from random import randint
    n = str(randint(10000000000, 99999999999))
    n = list(n)
    r1 = int(n[0]) * 10
    r2 = int(n[1]) * 9
    r3 = int(n[2]) * 8
    r4 = int(n[3]) * 7
    r5 = int(n[4]) * 6
    r6 = int(n[5]) * 5
    r7 = int(n[6]) * 4
    r8 = int(n[7]) * 3
    r9 = int(n[8]) * 2
    r10 = r1+r2+r3+r4+r5+r6+r7+r8+r9
    p0 = int(n[0]) * 11
    p1 = int(n[1]) * 10
    p2 = int(n[2]) * 9
    p3 = int(n[3]) * 8
    p4 = int(n[4]) * 7
    p5 = int(n[5]) * 6
    p6 = int(n[6]) * 5
    p7 = int(n[7]) * 4
    p8 = int(n[8]) * 3
    p9 = int(n[9]) * 2
    p10 = p0+p1+p2+p3+p4+p5+p6+p7+p8+p9
    rr = 11 - (r10 % 11)
    n[9] = int(n[9])
    c = c + 1
    print(c)
    if n[9] == rr:
        if rr > 9:
            rr = 0
    elif n[9] != rr:
        continue
    pp = 11 - (p10 % 11)
    n[10] = int(n[10])
    if n[10] == pp:
        if rr > 9:
            break
    elif n[10] != pp:
        continue
    no_cpf = ''
    for n_cpf in n:
        n[9] = str(n[9])
        n[10] = str(n[10])
        no_cpf += n_cpf
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11 = no_cpf
    print(f'{a1}{a2}{a3}.{a4}{a5}{a6}.{a7}{a8}{a9}-{a10}{a11}')
    break