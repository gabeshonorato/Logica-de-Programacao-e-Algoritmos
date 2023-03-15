print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplação')
print('/ Divisão')
print('PRESSIONE QUALQUER TECLA PARA SAIR')

while True:
    op = input('Qual operação você deseja fazer? ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor:'))
        y = int(input('Digite o segundo valor:'))

    if (op == '+'):
        res = x + y
        print ('Resultado: {} + {} = {}'.format(x,y, res))
        continue

    elif (op == '-'):
        res = x - y
        print ('Resultado: {} - {} = {}'.format(x,y, res))
        continue

    elif (op == '*'):
        res = x * y
        print ('Resultado: {} * {} = {}'.format(x,y, res))
        continue

    elif (op == '/'):
        res = x / y
        print ('Resultado: {} / {} = {}'.format(x,y, res))
        continue

    elif (op == 's'):
        break
    else:
        print ('Operação inválida!')


print('Encerrando o programa...')
