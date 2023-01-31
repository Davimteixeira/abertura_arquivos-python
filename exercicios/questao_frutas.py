# • peça para o usuário criar um dicionário com 10 frutas e o preço do quilo.
# • imprima o dicionário completo
# • imprima só os valores
# • imprima os itens com o mesmo valor de preço(se existir)
# • faça uma promoção e altere o valor de duas frutas para 1/3
# • insira duas novas frutas e seus preços
# • salve o dicionário em um arquivo
# • mostre qual fruta mais cara
# • apague o dicionário

frutas = dict ()
for i in range (10):
    f = input("diga uma fruta: ")
    v = float(input("diga o preço: "))
    frutas[f] = v

print (frutas) # dicionario de frutas
print (frutas.values()) #apenas os valores
frutas_duplicada = {}
for i,j in frutas.items():
    frutas_duplicada.setdefault(j, set()).add(i)
resultado =  [print(j,":",i) for i , j in frutas_duplicada.items() if len(j) > 1] #imprimir o mesmo valor se  existir

a = 0
for i,j in frutas.items(): #alterando valor de duas frutas
    if a < 2:
        frutas[i] = j * 0.3
        a += 1
    if a == 3:
        break   
print (frutas)

for i in range (2): # adicionado duas frutas no dicionario
    f = input("diga uma fruta: ")
    v = float(input("diga o preço: "))
    frutas[f] = v

print (frutas)

with open ("sacolao_da_aline.txt", "w", encoding="utf-8") as sacola: # escrevendo no arquivo

    [sacola.write(f'{chave}:{valor:.2f} \n') for chave, valor in frutas.items() ]

maior_valor = max(frutas, key = frutas.get) # fruta mais cara
print (f'{maior_valor}:{frutas[maior_valor]}')

del frutas # deletando o dicionario
print (frutas)