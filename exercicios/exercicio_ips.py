# minha resolucão
arquivo = open('ips.txt', 'r', encoding='utf8')
linhas = arquivo.readlines()
lista_octetos = []
for i in linhas:
    busca = i.find('.')
    lista_octetos.append(int(i[:busca]))
    lista_octetos.sort()
for i in lista_octetos:
    if i > 254:
        print(f'{i} - invalido')
    else:
        print(f'{i} - valido')
print(lista_octetos)
arquivo.close()

# resolusão do professor paulo
nova_lista= []
with open('ips.txt', 'r', encoding='utf8') as meus_ips:
    lista_ips = meus_ips.readlines()
    for linha in lista_ips:
        nova_linha = linha.replace('\n', '').split('.')
        del nova_linha[3]
        del nova_linha[2]
        del nova_linha[1]
        muda_tipo = int(nova_linha[0])
        nova_lista.append(muda_tipo)
        nova_lista.sort()
    while i in nova_lista:
        if i > 254 :
            print(f'{i} - invalido')
        else:
            print(f'{i} - valido')
        break
print(nova_lista)
    