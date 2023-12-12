import math
'''n1 = float(input('Qual é o tamanho do cateto oposto'))
n2 = float(input('Qual é o tamanho do cateto adjacente'))
cal = n1 + n2
raiz = math.sqrt(cal)
print('A soma dos catetos é {} e a ipoteniza é {}'.format(cal, raiz))'''

n1 = float(input('Qual é o tamanho do cateto oposto'))
n2 = float(input('Qual é o tamanho do cateto adjacente'))
hi = math.hypot(n1, n2)
print('A  ipoteniza é {:.2f}'.format( hi))