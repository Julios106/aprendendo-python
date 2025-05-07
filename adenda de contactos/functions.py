# 1. adicionar nome e telefone
lista = []


def adicionar():

    try:
        nome = input('Nome:')
        numero = int(input('Numero:'))

        while True:
            emaill = '@gmail.com'
            email = input('insira o email:'.title())

            if emaill not in email:
                print('Algo deu errado(formato do email incorreto)')
            else:
                break
        info = {
            'nome': nome,
            'numero': numero,
            'email': email
        }

        lista.append(info)

    except ValueError:
        print('Algo correu mal try again')

# 2. listar todos os contactos


def listar():
    for info in lista:
        print(
            f"nome:{info['nome']}|cont:{info['numero']}|email:{info['email']}".title())

# 3. Pesquisar por:


def pesquisar():
    print('1.Nome \n2.Numero \n3.Email')

    opcao2 = input('Opcao:')
    if opcao2 == '1':
        name = input('insira o nome :'.title())
        encontrado = False
        for info in lista:
            if name == info['nome']:
                print('Contacto encontrado!')
                print(
                    f"nome:{info['nome']}|cont:{info['numero']}|email:{info['email']}".title())
                encontrado = True
                break  # Adicionei um break para parar após encontrar
        if not encontrado:
            print('Contacto nao encontrado!')

    elif opcao2 == '2':
        try:
            encontrado2 = False
            number = int(input('digita o numero:'.title()))
            for info in lista:
                if number == info['numero']:
                    print('Contacto encontrado!')
                    print(
                        f"nome:{info['nome']}|cont:{info['numero']}|email:{info['email']}".title())
                    encontrado2 = True
                    break  # Adicionei um break para parar após encontrar
            if not encontrado2:
                print('Contacto nao encontrado!')

        except ValueError:
            print('Algo deu errado! Tente novamente')
    elif opcao2 == '3':
        encontrado3 = False
        gmail = input('Insira o Email:')
        for info in lista:
            if gmail == info['email']:
                print('Contacto encontrado!')
                print(
                    f"nome:{info['nome']}|cont:{info['numero']}|email:{info['email']}".title())
                encontrado3 = True
                break  # Adicionei um break para parar após encontrar
        if not encontrado3:
            print('Contacto encontrado!')
    else:
        print('opcao invalida'.upper())
