preco = float(input('Qual o valor do produto? '))
desc = (5 / 100) * preco
result = preco - desc

print('Seu produto foi de {:.2f} para {:.2f} com 5 de desconto'.format(preco, result))