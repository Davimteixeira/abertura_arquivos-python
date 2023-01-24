with open('abc1.txt', 'w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')
    
    file.seek(0)
    print(file.read())
    

with open('abc1.txt', 'r') as file:
    print(file.read())


with open('abc1.txt', 'a+') as file:
    file.write('outra linha\n')
    file.seek(0)
    print(file.read())

