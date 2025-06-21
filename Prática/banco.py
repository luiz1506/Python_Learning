def depositar(saldo, extrato):
    valor = float(input("Informe o valor de depósito: R$ "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(saldo, extrato):
    valor = float(input("Informe o valor e saque: R$"))
    if valor > 0:
        if valor <= saldo:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato

def visualizar_saldo(saldo, extrato):
    print("\n====EXTRATO====")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"Saldo autal: R$ {saldo:.2f}")
    print("============\n")

def menu():
    saldo = 0.0
    extrato = []

    while True:
        print("\n=====MENU=====")
        print("[1] - Depositar")
        print("[2] - Sacar")
        print("[3] - Visualizar Saldo")
        print("[0] - Sair")
        print("=============\n")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato = sacar(saldo, extrato)
        elif opcao == "3":
            visualizar_saldo(saldo, extrato)
        else:
            print("Opção inválida. Tente novamente.")

menu()




