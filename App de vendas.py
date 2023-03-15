#Definindo função para imprimir linhas
def linha(x):
    print(x*'-')


#Programa Principal

linha(46) #Chamando função
print('Bem-vindos a loja de Gabriela Froes Honorato!')
linha(46) #Chamando função


#Estrutura do Menu
print('                      MENU')

linha(46) #Chamando função
print('0 <= quantidade < 11      |    Valor R$ 30.00')
print('11  <= quantidade < 101   |    Valor R$ 60.00')
print('101 <= quantidade < 1001  |    Valor R$ 120.00')
print('quantidade >= 1001        |    Valor R$ 240.00')
linha(46) #Chamando função


#Entradas de pedidos dos usuários
valor = float(input("Qual o valor do produto?: "))
quantidade = float(input("Qual a quantidade do produto?: "))
frete = 0


#Início das condicionais para sabermos o valor do frete a ser pago
if (quantidade >= 0 and quantidade < 11):
    frete = 30.00

elif (quantidade >= 11 and quantidade <101):
    frete = 60.00

elif (quantidade >= 101 and quantidade < 1001):
    frete = 120.00

else:
    frete = 240.00



linha(46) #Chamando função
#Cálculos totais: Produtos e Fretes
total = quantidade * valor                  #Variável do total do produto
total_frete = total + frete                 #Variável do total do frete


#Exibindo Valores finais ao usuário
print('O valor total sem o frete R$: {:.2f}'.format(total))
print('O valor com o frete R$: {:.2f}'.format(total_frete))
print('Valor do frete R$: {:.2f}'.format(frete))


#Encerrando o programa
linha(63) #Chamando função
print('Muito obrigada por comprar na loja de Gabriela Froes Honorato!')
linha(63) #Chamando a função
