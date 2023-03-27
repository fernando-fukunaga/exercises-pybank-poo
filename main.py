from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

pybank = Banco()

cliente1 = Cliente("Fernando", 21)
conta1 = ContaCorrente("01", "222", 0.0)

cliente1.insere_conta(conta1)
pybank.insere_cliente(cliente1)
pybank.insere_conta(conta1)

escolha = 0

while escolha != 3:

    print("Bem vindo ao Pybank!")
    print("Escolha uma opção:\n1 - Depositar\n2 - Sacar\n3 - Encerrar")

    escolha = int(input("Digite o número: "))

    if escolha == 1:
        valor_deposito = input("\nDigite o valor a ser depositado: ")
        conta1.deposita(float(valor_deposito))

    elif escolha == 2:
        valor_saque = input("\nDigite o valor a ser sacado: ")
        if pybank.autentica(conta1, cliente1):
            print("Acesso ok")
            conta1.saca(float(valor_saque))
        else:
            print("Acesso negado!\n")