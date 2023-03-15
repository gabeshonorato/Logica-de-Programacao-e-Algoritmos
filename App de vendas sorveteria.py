#Definindo funções para linhas no código


def linha(x): #Função Linha caracterizada
    print(x*'*-')

def linha_comum(y): #Função Linha comum
    print(y*'-')

#Programa Principal

linha(28) #Chamando linha caracterizada
print('Olá!Bem-vindos a sorveteria da Gabriela Froes Honorato!')
linha(28)#Chamando linha caracterizada
print('\n') #Pulando linha para evitar poluição visual


#Exibindo Menu

linha(47) #Função Linha comum
print('                                           MENU')
linha(47) #Função Linha comum
print(' Código    Descrição      (Tamanho P - 500ML)     (Tamanho M - 1000ML)    (Tamanho G - 2000ML)')
linha_comum(94)
print(' TR          Sabores          R$: 6,00                R$: 10,00                R$: 18,00')
print('          Tradicionais')
linha_comum(94)
print(' ES          Sabores          R$: 7,00                R$: 12,00                R$: 21,00')
print('            Especiais')
linha_comum(94)
print(' PR          Sabores          R$: 8,00                R$: 14,00                R$: 24,00')
print('             Premium')
linha_comum(94)


valor = 0 #Definindo variável de valor

while True: #Criando um loop


#Recebendo as entradas de tamanhos e códigos desejado pelo usuário
    tamanho = input("Qual o tamanho do pote desejado? (p,m,g - minúsculo): ") #Recebe tamanho do pote
    codigo = input("Qual o codigo do sorvete desejado? (tr, es, pr - minúsculo): ") #Recebe código do sabor

#Iniciando as Condicionais
    if (tamanho == 'p' and codigo == 'tr' ):
        valor += 6.00 #Acrescentando valores a cada pedido

    elif (tamanho == 'm' and codigo == 'tr' ):
        valor += 10.00 #Acrescentando valores a cada pedido

    elif (tamanho == 'g' and codigo == 'tr' ):
        valor += 18.00 #Acrescentando valores a cada pedido

    elif (tamanho == 'p' and codigo == 'es' ):
        valor += 7.00 #Acrescentando valores a cada pedido

    elif (tamanho == 'm' and codigo == 'es' ):
        valor += 12.00 #Acrescentando valores a cada pedido

    elif (tamanho == 'g' and codigo == 'es' ):
        valor += 21.00 #Acrescentando valores a cada pedido

    elif (tamanho == 'p' and codigo == 'pr' ):
        valor += 8.00 #Acrescentando valores a cada pedido

    elif (tamanho == 'm' and codigo == 'pr' ):
        valor += 14.00 #Acrescentando valores a cada pedido

    elif (tamanho == 'g' and codigo == 'pr' ):
        valor += 24.00 #Acrescentando valores a cada pedido

    else: #Condicional inserida caso o usuário digite uma opção que não está no menu
        print('TAMANHO OU CÓDIGO INVÁlIDO')
        continue #volta para o início do loop

    opcao = input("Deseja mais alguma opção? (S/N): ")
    if (opcao == 's'):
        continue #volta para o menu
    else:
        break #encerra a opção de receber mais pedido


#Exibindo valores totais
linha_comum(47)
print('O valor total: R$ {:.2f}'.format(valor))
linha_comum(47)

print('\n') #Pulando linha para evitar poluição visual
linha(33)
print('Muito obrigada por comprar na sorvetria da Gabriela Froes Honorato')
linha(33)
