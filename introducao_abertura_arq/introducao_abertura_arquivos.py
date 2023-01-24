file = open('abc.txt','w+')
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')

#esse metodo faz com que o cursor volte para o inicio de tudo, e saia do fina. 
file.seek(0,0)
print('lendo linhas:')
# .read vai ler o arquivo inteiro e vai retornar uma string
print(file.read())
print('#################')

file.seek(0,0)
# o .readline ele vai ler linha por linha
# o end='' e para não mostrar a quebra de linha
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readlbine(), end='')
print('#################')

file.seek(0,0)
# o .redlines ele vai trazer os valores em uma lista
print(file.readlines())
print('#################')

file.seek(0,0)
# vai trazer os valores em um fo, linha por linha
for linha in file.readlines():
    print(linha, end='')
print('#################')

file.seek(0,0)
# vai trazer os valores em um fo, linha por linha
for linha in file:
    print(linha, end='')
print('#################')

file.close()