try:
    print(2+'casa')
except TypeError:
    print('ops deu erro!!')
    
    
try:
    print(x)
except:
    print('variavel x não está definida')
finally:
    print('o try except está finlizado')
    
    
try:
    print('Hello')
except:
    print('Algo deu errado')
else:
    print('nada deu errado')
    
