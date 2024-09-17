# Inicializando o saldo
saldo = float(input("Digite o saldo inicial: R$ "))
saldo_atual = saldo

# Função para sacar dinheiro
def sacar(saldo_atual):
    valor_solicitado = float(input("Digite o valor que deseja sacar: R$ "))
    if valor_solicitado > saldo_atual:
        print(f"Saldo insuficiente! Você tem R$ {saldo_atual:.2f} em sua conta bancária.")
    else:
        saldo_atual -= valor_solicitado
        print(f"Saque efetuado! Agora você tem R$ {saldo_atual:.2f} em sua conta.")
    return saldo_atual

# Função para depositar dinheiro
def depositar(saldo_atual):
    valor_deposito = float(input("Digite o valor que deseja depositar: R$ "))
    saldo_atual += valor_deposito
    print(f"Depósito efetuado! Agora você tem R$ {saldo_atual:.2f} em sua conta.")
    return saldo_atual

# Função para exibir o extrato
def extrato(saldo_atual):
    print(f"Você tem R$ {saldo_atual:.2f} em sua conta.")
    return saldo_atual

# Exibindo o extrato inicial
saldo_atual = extrato(saldo_atual)

# Realizando um saque
saldo_atual = sacar(saldo_atual)

# Realizando um depósito
saldo_atual = depositar(saldo_atual)

# Exibindo o extrato final
saldo_atual = extrato(saldo_atual)
