# função lambda

# caklcular imposto
preco = 1000
calcular_imposto = lambda x: x * 0.3
print(calcular_imposto(preco))

precos = [100, 500, 10, 25]
impostos = list(map(lambda x: x * 0.3, precos ))
# map vai pegar ums função e percorer por toos os valores