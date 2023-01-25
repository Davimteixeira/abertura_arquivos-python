lista_compras = [{"Descrição":"Água","preço":2.00},
                 {"Descrição":"Leite","preço":3.00},
                 {"Descrição":"Carne","preço":18.00},
                 {"Descrição":"Pizza","preço":9.00},
                 {"Descrição":"Chocolate","preço":6.50}
                 ]
print(f'''{lista_compras}\n
      A lista vai atualizar para um imposto de 10%''')
lista_do_imposto = list(map(lambda x:x["preço"]*0.10+x["preço"],lista_compras))
index= 0
for lista in lista_compras:
        lista["preço"] = lista_do_imposto[index]
        index += 1
print("*"*60)
print(f"A lista atualizada ficará:\n")
print(lista_compras)