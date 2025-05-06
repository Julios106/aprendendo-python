print('Bem Vindo ao Sistema de Análise de Notas')
print('Selecione uma opcao:')
print('1 - Cadastrar aluno')
print('2 - Exibir todos os alunos')
print('3 - Verificar aprovação por nome')
print('4 - Sair')
lista = []


def cadastro():
    try:
        nome = input('Nome do aluno:')
        idade = int(input('Idade:'))
        nota1 = []
        for i in range(3):
            nota = float(input(f'Insira a nota ({i + 1}/3):'))
            nota1.append(nota)
        media = sum(nota1) / len(nota1)

        info = {
            'nome': nome,
            'media': media,
            'idade': idade
        }

        lista.append(info)

    except ValueError:
        print('Algo deu errado')


def exibir():
    for info in lista:
        print(
            f"Nome:{info['nome']} | Idade:{info['idade']} | Media Final:{info['media']}")

        if info['media'] > 9:
            print('//Situacao:Aprovodo/a')
        else:
            print('//Situacao:Reprovado/a')


def verificar_aluno():

    verificar = input('Insira o nome que deseja encontrar no sistema:')
    encontrado = False

    for info in lista:
        if verificar == info['nome']:
            print(
                f"Nome:{info['nome']} | Idade:{info['idade']} | Media Final:{info['media']}")
            encontrado = True

    if not encontrado:
        print(f"{verificar} nao se cadastrou no sistema. ")


while True:
    opcao = input('opcao:')

    if opcao == '1':
        cadastro()
    elif opcao == '2':
        exibir()
    elif opcao == '3':
        verificar_aluno()
    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('Opcao invalida.')
