
import math
angulo = float(input('digite o angulo qie voce deseja'))
seno = math.sin(math.radians(angulo))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('o angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))

