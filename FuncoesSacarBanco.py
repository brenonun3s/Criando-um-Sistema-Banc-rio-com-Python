saldo = float = input();
saldoAtual = saldo;


def sacar() :
    valorSolicitado = input = int ("Digite o valor que deseja sacar : R$ \n")
    if valorSolicitado > saldo :
        print ("Saldo insuficiente !!!" "\n Você tem R$" + saldo + "em sua conta bancária")
    elif valorSolicitado <= saldo :
        saldoAtual = valorSolicitado - saldo
        print ("Saque efetuado!" "Agora você tem R$ " + saldoAtual + "em sua conta agora")

def depositar() :
    valorDeposito = input = int("Digite o valor que deseja depositar : R$ \n" )
    saldoDeposito = valorDeposito + saldoAtual
    return saldoDeposito

def extrato():
    print("Você tem R$" + saldoAtual + "em sua conta")
    return saldoAtual;
    
extrato();
sacar();
depositar();