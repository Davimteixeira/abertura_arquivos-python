numero = [int(input('informe um numero: '))]
numero_par = list(filter(lambda x: x %2 == 0, numero))
print(numero_par)