salario = float(input('qual é o seu salario? '))
aumento = (15 / 100) * salario
result = aumento + salario
print('seu atual salario é de R${:.2f} e com aumento de 15% passará a ser R${:.2f}'.format(salario, result))