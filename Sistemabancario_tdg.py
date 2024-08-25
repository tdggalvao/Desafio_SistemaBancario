from datetime import datetime

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []
        self.saques_diarios = []
        self.extrato.append(f"Abertura de conta com saldo inicial de R$ {saldo_inicial:.2f}")

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo!")
        else:
            self.saldo += valor
            self.extrato.append(f"Depósito de R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def pode_sacar(self, valor):
        hoje = datetime.now().date()
        saques_hoje = [saque for saque in self.saques_diarios if saque['data'] == hoje]

        if len(saques_hoje) >= 3:
            print("Limite de 3 saques diários atingido!")
            return False

        if valor > 500:
            print("O valor máximo por saque é de R$ 500,00!")
            return False

        if valor > self.saldo:
            print("Saldo insuficiente!")
            return False

        return True

    def sacar(self, valor):
        if self.pode_sacar(valor):
            self.saldo -= valor
            saque = {
                'data': datetime.now().date(),
                'valor': valor
            }
            self.saques_diarios.append(saque)
            self.extrato.append(f"Saque de R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def visualizar_extrato(self):
        print("\n--- Extrato da Conta ---")
        print(f"Titular: {self.titular}")
        for item in self.extrato:
            print(item)
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")


def criar_conta():
    titular = input("Digite o nome do titular da conta: ")
    while True:
        try:
            saldo_inicial = float(input("Digite o saldo inicial: "))
            if saldo_inicial < 0:
                raise ValueError("O saldo inicial não pode ser negativo.")
            break
        except ValueError as e:
            print(e)
    return ContaBancaria(titular, saldo_inicial)


def menu():
    conta = criar_conta()

    while True:
        print("\n--- Menu ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Visualizar Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                try:
                    valor = float(input("Digite o valor a depositar: "))
                    if valor <= 0:
                        raise ValueError("O valor do depósito deve ser positivo.")
                    break
                except ValueError as e:
                    print(e)
            conta.depositar(valor)

        elif opcao == "2":
            while True:
                try:
                    valor = float(input("Digite o valor a sacar: "))
                    if valor <= 0:
                        raise ValueError("O valor do saque deve ser positivo.")
                    break
                except ValueError as e:
                    print(e)
            conta.sacar(valor)

        elif opcao == "3":
            conta.visualizar_extrato()

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Escolha novamente.")


if __name__ == "__main__":
    menu()

