largura = float(input('qual a altura da parede? '))
altura = float(input('qual a largura da parede? '))
result = largura * altura
tinta = result / 2

print('voce precisa de {:.2f} litros de tinta para pintar {:.2f}m² de parede'.format(tinta, result))