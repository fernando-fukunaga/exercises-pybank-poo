from abc import ABCMeta, abstractmethod

class Banco:
    def __init__(self, contas, clientes):
        self._agencias = ["01","02","03","04"]
        self._contas = contas
        self._clientes = clientes

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta

class Conta:
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo
    def deposita(self, valor):
        self._saldo += valor
    def _dentro_do_limite(self, valor):
        return valor <= self._limite
    @abstractmethod
    def saca(self, valor):
        if self._dentro_do_limite(valor):
            self._saldo -= valor
        else:
            print('Sem limites você cara')
            
class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite):
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite
    def __str__(self):
        return f'Dados da conta:\nNome titular: {Cliente.nome}\nIdade titular: {Cliente.idade}\nAgência: {self._agencia}\nConta: {self._numero_conta}\nSaldo disp.: {self._saldo}\nLimite de saque: {self._limite}'

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)