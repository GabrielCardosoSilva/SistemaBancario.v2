def title(mensagem):
    print(f"\n{mensagem:=^30}")


def menu():
    title("MENU")

    print(f'''
{'—'*30}
[ d ] → Depositar
[ s ] → Sacar
[ e ] → Mostrar Extrato
[ n ] → Novo Usuario
[ c ] → Criar Conta Corrente
[ l ] → Mostra Lista de Contas
[ k ] → Mostra Contas Correntes
[ q ] → Sair do Programa
{'—'*30}
''')
    ordem = str(input("Escolha: ")).lower()[0]
    return ordem


def deposito(saldo, extrato):
    valor = float(input("Valor do Deposito: R$"))

    if valor > 0:
        saldo += valor
        extrato += f"\n{'Deposito':.<18}R${valor:>10.2f}"
        print(f"Deposito de R${valor:.2f} adicionado com Sucesso!\n")
    else:
        print("ERRO no Deposito, tente novament...\n")
    return saldo, extrato


def saque(saldo, extrato, limite):
    if limite > 0:
        valor = float(input("Valor do Saque: R$"))
        if valor > 0:
            saldo -= valor
            limite -= 1
            extrato += f"\n{'Saque':.<18}R${valor:>10.2f}"
            print(f"Saque de R${valor:.2f} retirado com Sucesso!")
        else:
            print("ERRO no Saque, tente novamente...")
    else:
        print("Limite de Saque alcançado, tente amanhã..")

    return saldo, extrato, limite


def extrato(saldo, extrato):
    print(f"\n{'='*30}\n{'Extrato Bancário':^30}\n{'='*30}")
    print("Não Houve Movimentações na conta" if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}\n{'='*30}")


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [digitos for digitos in usuarios if digitos['cpf'] in cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    cpf = str(input("Informe seu CPF (somente numeros): "))

    verificador = filtrar_usuarios(cpf, usuarios)

    if verificador:
        return print(f"O CPF:\'{cpf}\' já estra cadastrado")

    registro = dict()
    registro['nome'] = str(input("Nome: "))
    registro['nascimento'] = str(input("Data De Nascimento ( dd/ mm/ aaaa )"))
    registro['cpf'] = cpf
    registro['endereço'] = str(input("Endereço (logradouro, numero casa, bairro - cidade/sigla entado): "))
    print(f"Cliente {registro['nome']}, Cadastrado com Sucesso!!")
    return usuarios.append(registro.copy())


def mostrar_contas(usuarios):
    for contas in usuarios:
        print(f"{contas}\n")


def conta_corrente(agencia, numero, usuarios):
    title("Conta Corrente")
    cpf = str(input("Informe seu CPF(somente numeros): "))
    conta = filtrar_usuarios(cpf, usuarios)
    if conta:
        return {"agencia": agencia, "numero": numero, "usuario": conta}
    print("ERRO!! usuario não encontrado, criação de conta encerrado...")


def listar_contas(contas):
    for conta in contas:
        print(f'''
Agência:  {conta["agencia"]}
C/C:      {conta["numero"]}
Titular:  {conta["usuario"]["nome"]}
''')
        print("="*30)


def main():
    agencia = '0001'
    saldo = 0
    historico_bancario = ""
    limite_saque = 3
    lista_usuarios = []
    contas = []

    while True:
        escolha = str.lower(menu())

        if escolha in "q":
            title("ENCERRANDO")
            return print("\nFim do programa, Volte Sempre!!")

        elif escolha in "d":
            title("Deposito")
            saldo, historico_bancario = deposito(saldo, historico_bancario)

        elif escolha in "s":
            title("Saque")
            saldo, historico_bancario, limite_saque = saque(saldo=saldo, extrato=historico_bancario, limite=limite_saque)

        elif escolha in "e":
            title("Extrato")
            extrato(saldo, historico_bancario)

        elif escolha in "n":
            title("CRIAR USUARIO")
            criar_usuario(lista_usuarios)

        elif escolha in "l":
            title("Lista De Contas")
            mostrar_contas(lista_usuarios)

        elif escolha in "c":
            numero_conta = len(contas) + 1
            conta = conta_corrente(agencia, numero_conta, lista_usuarios)

            if conta:
                contas.append(conta)
                print("Conta Criada com sucesso!!")

        elif escolha in "k":
            title("CONTAS")
            listar_contas(contas)

        else:
            print("Opção invalida!")


main()
