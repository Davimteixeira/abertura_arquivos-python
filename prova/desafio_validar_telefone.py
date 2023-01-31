import re
dic_contatos = {}
with open('contatos.txt', 'r', encoding='utf8') as contatos:
    lista_contatos = contatos.readlines()
    for linha in lista_contatos:
        nova_linha = linha.replace('\n', '').split(':')  
        dic_contatos[str(nova_linha[0])]=str(nova_linha[1])
    for valor in dic_contatos.values():
        padrao_fixo = re.compile('(\([0-9]{2}\))([0-9]{4})-([0-9]{4})')
        padrao_celular = re.compile('(\([0-9]{2}\))([0-9]{5}).([0-9]{4})')
        busca_fixo = padrao_fixo.search(valor)
        busca_celuar = padrao_celular.search(valor)
        with open('novo_contato.txt', 'a', encoding='utf8') as novo_contato:
            if busca_fixo:
                novo_contato.write((valor + ':' + 'fixo') + '\n', )
            if busca_celuar:
                novo_contato.write((valor + ':' + 'celular') + '\n', )