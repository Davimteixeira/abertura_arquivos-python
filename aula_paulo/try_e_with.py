import os
# try:
#     arquivo = open('valida.txt', 'w', encoding='utf8')
#     arquivo.write('não é um teste de escrita')
# finally:
#     arquivo.close()
    

# with open('valida2.txt','w' , encoding='utf8') as meu_arquivo:
#     meu_arquivo.write('novo teste de não é o python')
    
# with open('valida2.txt','r' , encoding='utf8') as meu_arquivo:
#     print(meu_arquivo.read())

# os.rename('valida2.txt', 'alterado.txt')    
# os.remove('valida.txt')

lista = os.listdir()
print(lista)
print(lista[4])
