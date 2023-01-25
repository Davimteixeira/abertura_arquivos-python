# map aplica uma função em cada item de uma lista de itens

precos = [100, 1000, 900, 200,300]
precos_com_imposto = list(map(lambda x: x * 1.1, precos))
print(precos_com_imposto)
