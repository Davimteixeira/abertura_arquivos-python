# numeros pares digitados
numero = [int(input('informe um numero: '))]
numero_par = list(filter(lambda x: x %2 == 0, numero))
print(numero_par)

# numeros impar em lista
numero = [1,2,3,4,5,6,7,8,9,10]
numero_impar = list(filter(lambda x: x %2 == 1, numero))
print(numero_impar)