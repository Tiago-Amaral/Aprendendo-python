dias = int(input('quantos dias foi alugado? '))
km = float(input('quantos quilometros rodados? '))
resultdias = dias * 60
resultkm = km * 0.15
total = resultdias + resultkm
print('Voce alugou por {} dias, custou R${:.2f}, voce rodou {:.2f}Km e custou {:.2f}'.format(dias, resultdias, km, resultkm))
print('O total a pagar é de R${:.2f}'.format(total))

