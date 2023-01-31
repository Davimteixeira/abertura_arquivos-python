import re
with open("contatos.txt","r", encoding="utf8") as contatos:
    ler = contatos.readlines()
    padrao = re.compile("[(][0-9]{2}[)][0-9]{5}.[0-9]{4}")
    for i in ler:
        if padrao.search(i):
            i = i.replace("\n","")
            print(f"{i} : Valido")