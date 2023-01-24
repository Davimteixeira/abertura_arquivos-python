#  ESTRUTURA WITH

with open('meu_arquivo.txt', 'w',  encoding='utf8') as arquivo:
    arquivo.write('Meu_textooooooooooooooooo')

with open('meu_arquivo.txt', 'r') as arquivo:
    print(arquivo.read())
    