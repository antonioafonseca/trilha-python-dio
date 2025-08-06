menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0
# Deixei o valor do limite por saque como constante também.
VALOR_LIMITE_SAQUES = 500
QUANTIDADE_LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        entrada = input("Informe o valor do depósito: ")
        try:
            valor = float(entrada)
        except ValueError:
            print("Operação falhou! O valor informado é inválido.")
            continue

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        entrada = input("Informe o valor do saque: ")
        try:
            valor = float(entrada)
        except ValueError:
            print("Operação falhou! O valor informado é inválido.")
            continue

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > VALOR_LIMITE_SAQUES:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= QUANTIDADE_LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
