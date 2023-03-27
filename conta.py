from abc import ABC, abstractmethod
import time

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    def detalhes(self):
        print(f'\nDetalhes da conta:\nAgência: {self._agencia}\nNúmero da conta: {self._numero_conta}\nSaldo disponível: {self._saldo}\n')

    def deposita(self, valor):
        print("Efetuando operação...")
        time.sleep(2)        
        self._saldo += valor
        print(f'Depósito de {valor} reais efetuado!')
        self.detalhes()
    
    @abstractmethod
    def saca(self, valor):
        pass
            
class ContaCorrente(Conta):
    def saca(self, valor):
        print("Efetuando operação...")
        time.sleep(2)        
        if self._saldo < valor:
            print("Saldo indisponível!!\n")
        else:
            self._saldo -= valor
            print(f'Saque de {valor} reais efetuado!')
            self.detalhes()

class ContaPoupanca(Conta):
    def saca(self, valor):
        print("Efetuando operação...")
        time.sleep(2) 
        if self._saldo < valor:
            print("Saldo indisponível!!\n")
        else:           
            self._saldo -= valor
            print(f'Saque de {valor} reais efetuado!')            
            self.detalhes()