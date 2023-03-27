import time

class Banco:
    def __init__(self):
        self._agencias = ["01","02","03","04"]
        self._contas = []
        self._clientes = []

    def insere_conta(self, conta):
        self._contas.append(conta)

    def insere_cliente(self, cliente):
        self._clientes.append(cliente)

    def autentica(self, conta, cliente):
        print("Autenticando o cliente...")
        time.sleep(3)
        return conta in self._contas and cliente in self._clientes and conta._agencia in self._agencias