
arquivo =open('dom_casmuro.txt','r', encoding='utf8')
quantidade = 0
palavras =[]
y = 0
for linha in arquivo :
    linha = linha.rstrip()
    linha = linha.lstrip()
    #print('Linha original ', linha)
    p = linha.split(' ')
    # print('linha processada ', p)
    palavras = palavras + p

# print(palavras)

arquivo.close()
palavra_busca = input ('Digite a palavra desejada: ')

for palavra in palavras:
    if palavra_busca == palavra:
        quantidade = quantidade + 1
    if palavra[0:len(palavra_busca)] == palavra_busca:
        quantidade = quantidade + 1
print(quantidade)

arquivo.close()