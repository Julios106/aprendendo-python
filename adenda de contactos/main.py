import functions

print('//agenda de contactos//'.upper())
print('1. adicionar nome e telefone'.title())
print('2. listar todos os contactos'.title())
print('3. Pesquisar por: ')
print('4. Sair')

while True:
    opcao = input('Selecione uma opcao;')

    if opcao == '1':
        functions.adicionar()
    elif opcao == '2':
        functions.listar()
    elif opcao == '3':
        functions.pesquisar()
    elif opcao == '4':
        print('SAINDO...')
        break
    else:
        print('opcao invalida'.upper())
