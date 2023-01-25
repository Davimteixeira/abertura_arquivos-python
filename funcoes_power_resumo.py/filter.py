# a função precisa ter uma logica de fitrar e precisa ser um interavel
idades = [12, 28 ,34 , 45 , 46 , 39 ]

filtrar_lista = list(filter(lambda x : x > 20, idades))
print(filtrar_lista)

lista_nomes = ['davi', 'magalhaes', 'teixeira']

filtrar_nomes = list(filter(lambda x: x in 'davi', lista_nomes))
print(filtrar_nomes)