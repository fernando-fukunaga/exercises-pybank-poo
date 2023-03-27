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
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = None

    def insere_conta(self, conta):
        self._conta = conta

    def __str__(self):
        return f'Dados da conta:\nNome titular: {self.nome}\nIdade titular: {self.idade}\nAgência: {self._conta._agencia}\nConta: {self._conta._numero_conta}\nSaldo disp.: {self._conta._saldo}'