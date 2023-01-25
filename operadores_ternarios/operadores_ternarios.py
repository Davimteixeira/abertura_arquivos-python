user_log = False

if user_log == True:
    msg = 'Usuario logado com sucesso'
else:
    msg = 'Login incorreto. verifique seu usuário ou sua senha'

print(msg)

# operador ternario 
user_log = True
msg = 'Usuario Logado com sucesso!' if (user_log) else 'Login incorreto, verifique seu usuario ou sua senha'
print(msg)

idade = input('informe sua idade: ')
if not idade.isnumeric():
    print('voce precisa digitar somente numeros')
else:
    idade = int(idade)
    eh_de_maior = (idade >= 18)
    eh_adolescente = (idade > 12 and idade < 18)
    msg = 'você é de maior parabéns, ja pode ser preso' if eh_de_maior else 'você é adolecente!!' if eh_adolescente else 'Você é criança'
    print(msg)