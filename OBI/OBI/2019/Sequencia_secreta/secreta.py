itr = int(input())
if 1<= itr <= 500:
    s = []
    possiblities = 0
    for c in range(itr):
            x = int(input())
            if x == 1 or x == 2:
                s.append(x)
            else:
                print('Erro Recomeçe')
    for elem in range(len(s)-1):
        if s[elem] == s[elem+1]:
            possiblities += 1
    print(itr - possiblities)