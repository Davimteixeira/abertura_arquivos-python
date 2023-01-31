# resolução pv
with open("alunos.txt", "r", encoding="utf8") as alunos:
    dici = set()
    ler = alunos.readlines()
    for i in ler:
        i = i.replace("\n", "").split(":")
        dici.add((f"{i[0].lower()}:{i[1]}"))
dici = sorted(dici, key = lambda x:x[0])
print(dici)
with open("alunos_orgainzado.txt", "w" , encoding="utf8") as aluno:
    for d in dici:
        aluno.write(f"{d}" + "\n")
         
# sara fez 
def segundo_item(item):
    return item
nova_lista = set()
altera_tipo = set()
with open("nomes.txt", "r", encoding="utf8") as notas:
    lista_notas = notas.readlines()
    for linha in lista_notas:
        nova_linha = linha.replace('\n', '').split(':')
        altera_tipo = (nova_linha[0].lower(),float(nova_linha[1]))
        nova_lista.add(altera_tipo)
    a=sorted(nova_lista,key=segundo_item)
    print(a)
with open('novo_nome.txt','a',encoding='utf-8') as arquivo:
    for n in a:
        n=str(n)
        arquivo.write(n +'\n')