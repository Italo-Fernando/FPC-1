n = int(input())
predios = [int(elem) for elem in input().split()]
#list comprehension
distancia = 0
primeiro_predio = 0
l = len(predios)

if n == l:
    for i in range(n):
        d = predios[0] + i + predios[i] #distancia de manhattan
        if d > distancia:
            distancia = d
            primeiro_predio = i # verificamos o predio mais distante
    
    distancia_final = 0
    for f in range(n):
        if primeiro_predio != f:
            distancia_final = max(distancia_final,predios[primeiro_predio] + abs(primeiro_predio-f) + predios[f])#verificamos a distancia do amigo mais distante do primeiro predio
else:
    None
   
print(distancia_final)