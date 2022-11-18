"""
CPF = 168.995.350-09
--------------------------------------------------
1 * 10 = 10          #        1 * 11 = 11 <-
6 * 9 = 54           #        6 * 10 = 60
8 * 8 = 64           #        8 * 9 = 72
9 * 7 = 63           #        9 * 8 = 72
9 * 6 = 54           #        9 * 7 = 63
5 * 5 = 25           #        5 * 6 = 30
3 * 4 = 12           #        3 * 5 = 15
5 * 3 = 15           #        5 * 4 = 20
0 * 2 = 0            #        0 * 3 = 0
                     #      ->0 * 2 = 0
        297          #                343
11 - (297 % 11) = 11 #         11 - (343 % 11) = 9
11 > 9 = 0           #
Digito 1 = 0         #        Digito 2 = 9
"""
cpf = input("Digite seu CPF: ")
n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = cpf
r1 = int(n1) * 10
r2 = int(n2) * 9
r3 = int(n3) * 8
r4 = int(n4) * 7
r5 = int(n5) * 6
r6 = int(n6) * 5
r7 = int(n7) * 4
r8 = int(n8) * 3
r9 = int(n9) * 2
r10 = r1+r2+r3+r4+r5+r6+r7+r8+r9
p0 = int(n1) * 11
p1 = int(n2) * 10
p2 = int(n3) * 9
p3 = int(n4) * 8
p4 = int(n5) * 7
p5 = int(n6) * 6
p6 = int(n7) * 5
p7 = int(n8) * 4
p8 = int(n9) * 3
p9 = int(n10) * 2
p10 = p0+p1+p2+p3+p4+p5+p6+p7+p8+p9
rr = 11 - (r10 % 11)
if rr > 9:
    rr = 0
pp = 11 - (p10 % 11)
if pp > 9:
    pp = 0
no_cpf = ''
for n_cpf in cpf:
    no_cpf += n_cpf
n10 = int(n10)
n11 = int(n11)
sequencia = no_cpf == str(no_cpf[0]) * len(cpf)
if rr == n10 and not sequencia:
    if pp == n11:
        print(f'CPF VALIDO "{no_cpf}"')
    else:
        print('CPF INVALIDO')
else:
    print('CPF INVALIDO')