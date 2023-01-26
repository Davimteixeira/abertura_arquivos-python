# Faça a verificação de cada funcionário para aplicar o valor de desconto no valor de salario de cada um. Crie um novo arquivo com os funcionários e os novos salários.

descontos_funcionarios = {}
valor_desconto = {}
with open('funcionarios.txt', 'r', encoding='utf-8') as funcionario:
    funcionarios = funcionario.readlines()
    for linha in funcionarios:
        nova_linha = linha.replace('\n', '').split(':')  
        descontos_funcionarios[str(nova_linha[0])]=float(nova_linha[1])
        for v in descontos_funcionarios.values():
            valor = (v == 1500.00)
            conta = (1500.00 + 1500.00 * 0.13)
            conta_1 = (1200.00 + 1200.00 * 0.07)
        with open('desconto_funcionarios.txt' , 'a', encoding='utf8') as arquivo:
            if valor:
                arquivo.write(nova_linha[0] + ':')
                arquivo.write(str(conta) + '\n')
            if valor == False:
                arquivo.write(nova_linha[0] + ':')
                arquivo.write(str(conta_1) + '\n')
    
    arquivo = open('desconto_funcionarios.txt', 'r', encoding='utf8') 
    print(f'o salario dos funcionarios com descontos é de \n{arquivo.read()}')
            
            