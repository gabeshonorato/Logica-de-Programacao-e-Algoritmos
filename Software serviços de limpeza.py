#Definindo as funções

def linha(x): #função tabela do nome
    print(x*'.~')

def linha_comum(y): #função linha comum
    print(y*'-')

def linha_personalizada(a): #função da linha personalizada
    print(a*'--*')

#Programa Principal
linha(37) #chamando linha
print(' Bem vindos ao Programa de Serviços de Limpeza da Gabriela Froes Honorato')
linha(37) #chamando linha
print('\n') #pulando linha para evitar a poluição visual


#Exibindo menu com valores
linha_comum(50) #chamando linha comum
print('                    MENU') #chamando menu
linha_comum(50) #chamando linha comum

print('\n') #pulando linha para evitar a poluição visual
linha_personalizada(17) #chamando linha personalizada
print('              Metragem vs valor')
linha_personalizada(17) #chamando linha personalizada
linha_comum(50) #chamando linha comum
print('Metragem (m²)             Valor (R$)')
linha_comum(47) #chamando linha comum
print('30 <= metragem < 300  |  60 + 0.3* metragem  |')
print('300 <= metragem < 700 |  120 + 0.5* metragem |')
print('Outros valores        |  Não são aceitos     |')
linha_comum(47) #chamando linha comum
print('\n') #pulando linha para evitar a poluição visual


#Exibindo menu com valores
linha_personalizada(17) #chamando linha personalizada
print('         Tipo Versus Multiplicador')
linha_personalizada(17) #chamando linha personalizada
linha_comum(50) #chamando linha comum
print('          Tipo             Multiplicador')
linha_comum(50) #chamando linha comum
print('B - Básica: Indicada para              |  1,00  |')
print('sujeiras semanas ou quinzenais         |        |')
linha_comum(50)
print('C - Completa: Indicada para            |  1,30  | ')
print('sujeiras antigas e/ ou não rotineiras  |        |')
linha_comum(50) #chamando linha comum
print('\n') #pulando linha para evitar a poluição visual


#Exibindo menu com valores
linha_personalizada(17) #chamando linha personalizada
print('            Adicionais versus valor')
linha_personalizada(17) #chamando linha personalizada
linha_comum(50) #chamando linha comum
print('          Adicionais                   Valor')
linha_comum(50) #chamando linha comum
print('0- Não desejo mais nada (encerrar)  |  0,00  |')
print('1- Passar 10 peças de roupas        |  10,00 |')
print('2- Limpeza de 1 forno/micro-ondas   |  12,00 |')
print('3- Limpeza de 1 geladeira/Freezer   |  20,00 |')
linha_comum(47) #chamando linha comum


#Definindo função para metragem
def metragem_limpeza():
    valor = 0 #variáveis para armazenar valores
    metragem = 0 #variáveis para armazenar valores


    try: #chamando try para tratamento de erros
        metragem = int(input('Qual a metragem (m²)?:  ')) #recebendo dado do usuário
    except:
        print('Digite um valor numérico: ')

#Chamando condicionais
    if (metragem >= 30 and metragem < 300 ):
        valor = (60 + (0.3* metragem))
        print('É necessário contratar 1 pessoa! ')


    elif (metragem >= 300 and metragem <700):
        valor = (120 + (0.5* metragem))
        print('É necessário contratar 2 pessoas! ')

#Definindo o else caso o usuário digite algo diferente do esperado
    else:
        print('Você digitou um valor de metragem que não trabalhamos...')
        print('Reveja o menu!')
        metragem_limpeza() #retornando a entrada de dados

    return valor #para retornar o valor




#Definindo o tipo de limpeza
def tipo_limpeza():
    multi = 0


    limpeza = input("Qual o tipo da limpeza?: (a/b) ") #recebendo dado do usuário

#Chamando condicionais
    if (limpeza == 'a'):
        multi = 1.00

    elif (limpeza == 'b'):
        multi = 1.30

    else:
        print('Não trabalhamos com esse tipo de limpeza...')
        print('Reveja o menu!')

        metragem_limpeza() #retornando a entrada de dados

    return multi #para retornar o valor


#Definindo função para adicionais na limpeza
def adicional_limpeza():
    valor = 0
    adicionais = input('Deseja adicionais?:  ')

#Iniciando as condicionais
    if (adicionais == '0'):
        valor = 0

    elif (adicionais == '1'):
        valor = 10.00

    elif (adicionais == '2'):
        valor = 12.00

    elif (adicionais == '3'):
        valor = 20.00

    else:
        print('Opção inválida...')
        print('Reveja o menu!')

    return valor #para retornar o valor

#Iniciando os cálculos
linha_personalizada(17) #chamando linha personalizada
valor_metro = metragem_limpeza()
valor_limpeza = tipo_limpeza()
valor_adicional = adicional_limpeza()

#Cálculos de valores
total = (valor_metro * valor_limpeza) + valor_adicional
print('Valor total: R$ {} - Valor metro: R$ {} - Tipo: {} - Adicionais: R$ {} '.format(total,valor_metro, valor_limpeza, valor_adicional))

print('\n') #pulando linha para evitar a poluição visual
linha(47) #chamando linha
print(' Muito Obrigada por comprar no Programa de Serviços de Limpeza da Gabriela Froes Honorato')
linha(47) #chamando linha



















