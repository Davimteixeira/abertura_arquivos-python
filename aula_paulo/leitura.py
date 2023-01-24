leitura = open('valida2.txt', 'r' , encoding='utf-8')
leitura.seek(5)
corte = leitura.read(5)
print(corte)