import re

arquivo =open('dom_casmuro.txt','r', encoding='utf8')
palavras = []
y = 0
for linha in arquivo :
    linha = linha.rstrip()
    linha = linha.lstrip()
    p = linha.split(' ')
    palavras = palavras + p
    
arquivo.close()
def digita_palavra():
    quantidade = 0
    palavra_busca = input('Digite a palavra desejada: ')
    padrão = re.compile('[A-Za-záàâãéèêíïóòôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]{3,}')
    busca = padrão.match(palavra_busca)
    if busca:
        for palavra in palavras:
            if palavra_busca == palavra:
                quantidade = quantidade + 1
            if palavra[0:len(palavra_busca)] == palavra_busca:
                quantidade = quantidade + 1
    else:
        print('fora do padrão')
        digita_palavra() 
    print(f'a palavra é {palavra_busca} e apareceu: {quantidade} vezes')
arquivo.close()

digita_palavra()


import re
entrada_palavra = str(input("Digite uma palavra para encontrar sua recorrência no texto:"))
padrão = re.compile('[A-Za-záàâãéèêíïóòôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]{3,}')
busca = padrão.match(entrada_palavra)
if busca:
    with open ("dom_casmuro.txt", "r",encoding="utf8") as leitura:
        texto = (leitura.read()).lower()
        padrão_palavra = ("\s"+entrada_palavra+"\s").lower()
        busca_texto = re.findall(padrão_palavra,texto)
        print(len(busca_texto))
else:
    raise ValueError('Palavra inválida')