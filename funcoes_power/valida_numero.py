# numeros pares digitados
numero = [int(input('informe um numero: '))]
numero_par = list(filter(lambda x: x %2 == 0, numero))
print(numero_par)

# numeros impar em lista
numero = [1,2,3,4,5,6,7,8,9,10]
numero_impar = list(filter(lambda x: x %2 == 1, numero))
print(numero_impar)

# calculando imposto
numero = [100,200,300,400,500,600,700,800,900,100]
adiciona_imposto = list(map(lambda x : x * 0.15, numero))
print(adiciona_imposto)

alunos = [{'nome' : 'aurelice', 'matricula' : 1000}, {'nome': 'sara', 'matricula': 1100}, {'nome': 'aline', 'matricula':1200}]
verifica_matricula = list(filter(lambda x: x['matricula'] >= 1100, alunos))
print(verifica_matricula)