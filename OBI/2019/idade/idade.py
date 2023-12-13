M = int(input())
A = int(input())
B = int(input())
if A!=B and 1<=A<=M and 1<=B<=M:
    C = M-(A+B)
    R1 = bool(A>B and A>C)
    R2 = bool(B > C)
    if R1:
        resposta = A
    elif R2:
        resposta = B
    else:
        resposta = C

print(resposta)
