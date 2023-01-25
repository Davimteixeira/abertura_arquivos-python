# vai elaborar um codico que leia os valores de valores.txt
# e implemente um novo arquivo chamado pagamentos.txt com a seguinte estrutura bidimensional
# solicite os tres nomes dos funcionarios.
# nome: valor

def leitura():
    arquivo = open('valores.txt', 'r')
    for linha in arquivo:
        print(linha.strip())
    arquivo.close()
    return None
def pagamentos():
    arquivo = open('valores.txt','r')
    arquivo2 = open('pagamentos.txt','w')
    for linha in arquivo:
        nome = input('digite um nome: '.strip())
        arquivo2.write(nome+' : ')
        arquivo2.write(linha)
    arquivo.close()
    arquivo2.close()
    arquivo3 = open('pagamentos.txt', 'r')
    for linha in arquivo3:
       print(linha.strip())
    arquivo3.close()
    return None

    
leitura()
pagamentos()

# valor = open('valores.txt', 'r')
# pag_valor = open('pagamentos.txt', 'r')

# for linha in valor:
#     nome = input('digite um nome: ')
#     pag_valor.write(nome + ':' + linha)
# valor.close()
# pag_valor.close()

# pag_valor = open('pagamento.txt', 'r')
# for linha in pag_valor:
#     print(linha)
    

