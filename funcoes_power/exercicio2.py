lista_valores = []
for x in range(5):
    numero = int(input('Digte 5 numeros: '))
    lista_valores.append(numero)
    lista_valores.sort()
menor_numero = lambda : lista_valores[0] * 3
maior_numero = lambda :lista_valores[4] * 2
maior_que_vinte = list(filter(lambda x: x > 20, lista_valores))

print(lista_valores)
print(f'os numeros maior que 20 são:{maior_que_vinte}')
print(f'o dobro do maior numero é {maior_numero()}')
print(f'o triplo do menor numero é {menor_numero()}')