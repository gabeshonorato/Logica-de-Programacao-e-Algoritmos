# ------------------------- Variáveis ------------------------------------
lista_funcionarios = []                                                               #Variável para uma lista no dicionário
id_desejado = 0
consulta = 0
id_func = 0

#-------------------------funções linhas --------------------------------
def linha_comum(x): #função para linha comum
    print(x*'-')

def linha_personalizada(x): #função para linha personalizada
    print(x*'*~*')

# ----------------- Cadastramento funcionários ---------------------------
def cadastrar_funcionarios(id_func): #Função cadastrar funcionários

    print('Insira os dados sobre um novo funcionário')
    nome = input('NOME completo do Funcionário: ')
    salario = input('Insira o SALÁRIO do Funcionário: ')
    setor = input('SETOR de trabalho do usuário: ')
    dicionario_funcionarios = {'identificador' : id_func, 'nome' : nome, 'salário' : salario, 'Setor' : setor}   #criando dicionário para exibir os funcionários cadastrados

    lista_funcionarios.append(dicionario_funcionarios.copy()) #Criando lista de dados armazenados no dicionário
# ----------------- Fim do cadastramento ---------------------------------


# ----------------- Consultar funcionários --------------------------------
def consultar_funcionarios(): #Função consultar funcionários
    while True:
        opcao_consultar = input('Escolha a opção que deseja consultar\n ' #Entrada de dados para o usuário definir o que desejar realizar
                      ''+ '1 - Consultar todos os funcionários\n ' +
                      '2 - Consultar funcionário por id\n ' +
                      '3 - Consultar um funcionário por setor\n ' +
                      '4 - Retornar\n'
                      '--> : ')

#Iniciando as condicionais
        if opcao_consultar == '1':
            print('Você selecionou a opção consultar TODOS funcionários')
            linha_comum(50) #chamando função de linha
            for funcionario in lista_funcionarios:
                for key, value in funcionario.items():
                    print('{}:  {}'.format(key, value)) #percorrendo dicionário para encontrar dados sobre todos os funcionários
                linha_comum(50) #chamando função de linha


        elif opcao_consultar == '2':
            print('Você selecionou a opção consultar TODOS funcionários')
            linha_comum(50)
            id_desejado = int(input('Insira o ID que deseja consultar: '))
            for funcionario in lista_funcionarios:
                if funcionario['identificador'] == id_desejado:
                    for key, value in funcionario.items(): #percorrendo dicionário para encontrar dados sobre o id
                        print('{}:  {}'.format(key, value))


        elif opcao_consultar == '3':
            print('Você selecionou a opção consultar funcionário por setor')
            setor_desejado = input('Insira o SETOR que deseja consultar: ')
            for funcionario in lista_funcionarios:
                if funcionario['Setor'] == setor_desejado:
                    for key, value in funcionario.items(): #percorrendo dicionário para encontrar dados sobre o setor
                        print('{}:  {}'.format(key, value))

        elif opcao_consultar == '4':
            print('Você está retornando ao menu anterior... ')
            return

        else:
            print('Opção inválida!!! Tente novamente. ' )
            continue
# ----------------- Fim das consultas de funcionários ----------------------


# ----------------- Removendo funcionários ----------------------------------
def remover_funcionarios(): #Função remover funcionários
    print('Bem vindos a opção de remover funcionários')
    id_desejado = int(input('Insira o ID do funcionário que você deseja remover: '))
    for funcionario in lista_funcionarios:
        if funcionario['identificador'] == id_desejado:
            lista_funcionarios.remove(funcionario) #removendo um funcionário da lista de funcionários
            print('Funcionário removido!')

# ----------------- Fim da opção de remover funcionários ----------------------

#-------------------- Programa Principal --------------------------------------
linha_personalizada(27)
print(' Bem vindos ao software de controle de funcionários da Gabriela Froes Honorato')
linha_personalizada(27)



while True:
    opcao = input('Escolha a opção desejada\n ' #Entrada de dados sobre a opção desejada pelo usuário
                  ''+ '1 - Cadastrar um funcionário\n ' +
                  '2 - Consultar funcionários\n ' +
                  '3 - Remover um funcionário\n ' +
                  '4 - Sair\n'
                  '--> : ')

    # Iniciando as condicionais
    if opcao == '1':
        id_func += 1 #definindo variável de identificação do funcionário
        cadastrar_funcionarios(id_func) #chamando função de cadastramento
        linha_comum(50)
        print('                 CADASTRADO      ')
        linha_comum(50)
        for funcionario in lista_funcionarios:
            for key, value in funcionario.items(): #percorrendo dicionário para encontrar dados sobre um funcionário recém cadastrado
                print('{}:  {}'.format(key, value)) #exibindo dados do dicionário
        linha_comum(50)

    elif opcao == '2':
        consultar_funcionarios() #chamando função para consultas de funcionário

    elif opcao == '3':
        remover_funcionarios() #chamando função para remover um funcionário

    elif opcao == '4':
        print('Você está saindo do menu de opções... ')
        linha_personalizada(30)
        print(' Muito obrigada por usar o software de controle de funcionários da Gabriela Froes Honorato')
        linha_personalizada(30)
        break #Encerrando o software

    else: #Condicional para verificar se o usuário esta digitando um opção válida
        print('Opção inválida!!! Tente novamente. ' )
        continue




