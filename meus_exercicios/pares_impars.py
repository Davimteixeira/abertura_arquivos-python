# Crie um programa que leia os arquivos pares.txt e ímpares.txt e que 
# crie um só arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos, 
# de forma a preservar a ordem numérica
conjunto_organizado = set()
lista_completa = []

with open('pares.txt', 'r', encoding='utf8') as pares:
    arquivo = pares.readlines()
    for linha in arquivo:
        nova_linha = linha.replace('\n', '').split(':')
        lista_completa.append(nova_linha)
        convert = set(lista_completa)
        print(nova_linha)
        
with open('impars.txt', 'r' , encoding='utf8') as impars:
    arquivo2 = impars.readlines()
    for linhas in arquivo2:
        nova_linha1 = linhas.replace('\n', '').split(':')
        lista_completa.append(nova_linha1)
        convert = set(lista_completa)
        print(nova_linha1)
        
# FALTA TERMINAR ESSE EXERCICIO