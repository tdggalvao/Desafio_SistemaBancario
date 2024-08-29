from datetime import datetime

# Armazenar os usuários e contas bancárias
usuarios = []
contas = []

# Função para criar um usuário (cliente)
def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Verificar se o CPF já existe
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado! Não é possível cadastrar dois usuários com o mesmo CPF.")
        return None
    # Criar e adicionar usuário à lista
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuario

# Função para criar uma conta corrente
def criar_conta_corrente(usuario):
    # Número sequencial para a conta
    numero_conta = len(contas) + 1
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario,
        'saldo': 0,
        'extrato': [],
        'saques_diarios': [],
        'numero_saques': 0,
        'limite_saques': 3,
        'limite_saque': 500
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {conta['agencia']} | Número da Conta: {conta['numero_conta']}")
    return conta

# Função para realizar saque (argumentos apenas por nome)
def sacar(*, saldo, valor, extrato, numero_saques, limite_saque, limite_saques, saques_diarios):
    hoje = datetime.now().date()
    saques_hoje = [saque for saque in saques_diarios if saque['data'] == hoje]

    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido!")
    elif valor > limite_saque:
        print("O valor máximo por saque é de R$ 500,00!")
    elif valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        numero_saques += 1
        saque = {'data': hoje, 'valor': valor}
        saques_diarios.append(saque)
        extrato.append(f"Saque de R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    return saldo, extrato

# Função para realizar depósito (argumentos apenas por posição)
def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("O valor do depósito deve ser positivo!")
    else:
        saldo += valor
        extrato.append(f"Depósito de R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    return saldo, extrato

# Função para visualizar o extrato (argumentos por posição e nome)
def visualizar_extrato(saldo, *, extrato):
    print("\n--- Extrato da Conta ---")
    for item in extrato:
        print(item)
    print(f"Saldo atual: R$ {saldo:.2f}\n")

# Função para listar usuários cadastrados
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']} | CPF: {usuario['cpf']}")

# Função para listar contas cadastradas
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']} | Número da Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")

# Menu principal
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Visualizar Extrato")
        print("6. Listar Usuários")
        print("7. Listar Contas")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            cpf = input("Digite o CPF (apenas números): ")
            endereco = input("Digite o endereço (Logradouro, nº, Bairro, Cidade, UF): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "2":
            cpf = input("Digite o CPF do usuário para criar a conta: ")
            usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
            if usuario:
                criar_conta_corrente(usuario)
            else:
                print("Usuário não encontrado!")

        elif opcao == "3":
            cpf = input("Digite o CPF do titular da conta: ")
            usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
            if usuario:
                conta = next((c for c in contas if c['usuario'] == usuario), None)
                if conta:
                    valor = float(input("Digite o valor a depositar: "))
                    conta['saldo'], conta['extrato'] = depositar(conta['saldo'], valor, conta['extrato'])
                else:
                    print("Conta não encontrada!")
            else:
                print("Usuário não encontrado!")

        elif opcao == "4":
            cpf = input("Digite o CPF do titular da conta: ")
            usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
            if usuario:
                conta = next((c for c in contas if c['usuario'] == usuario), None)
                if conta:
                    valor = float(input("Digite o valor a sacar: "))
                    conta['saldo'], conta['extrato'] = sacar(
                        saldo=conta['saldo'],
                        valor=valor,
                        extrato=conta['extrato'],
                        numero_saques=conta['numero_saques'],
                        limite_saque=conta['limite_saque'],
                        limite_saques=conta['limite_saques'],
                        saques_diarios=conta['saques_diarios']
                    )
                else:
                    print("Conta não encontrada!")
            else:
                print("Usuário não encontrado!")

        elif opcao == "5":
            cpf = input("Digite o CPF do titular da conta: ")
            usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
            if usuario:
                conta = next((c for c in contas if c['usuario'] == usuario), None)
                if conta:
                    visualizar_extrato(conta['saldo'], extrato=conta['extrato'])
                else:
                    print("Conta não encontrada!")
            else:
                print("Usuário não encontrado!")

        elif opcao == "6":
            listar_usuarios()

        elif opcao == "7":
            listar_contas()

        elif opcao == "8":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Escolha novamente.")

if __name__ == "__main__":
    menu()

