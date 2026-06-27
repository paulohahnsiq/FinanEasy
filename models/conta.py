from models.cliente import Cliente
from models.transacao import Transacao


class SaldoInsuficienteError(Exception):
    """Levantada quando uma operação tenta sacar/transferir mais do que o saldo disponível."""


class ValorInvalidoError(Exception):
    """Levantada quando um valor de operação é inválido (zero ou negativo)."""


class Conta:
    """Representa uma conta bancária e suas operações."""

    def __init__(self, numero: str, cliente: Cliente, saldo: float = 0.0, transacoes=None):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.transacoes = transacoes or []

    def depositar(self, valor: float, descricao: str = "Depósito em conta") -> None:
        if valor <= 0:
            raise ValorInvalidoError("O valor do depósito deve ser maior que zero.")
        self.saldo += valor
        self.transacoes.append(Transacao("deposito", valor, descricao))

    def sacar(self, valor: float, descricao: str = "Saque em conta") -> None:
        if valor <= 0:
            raise ValorInvalidoError("O valor do saque deve ser maior que zero.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor
        self.transacoes.append(Transacao("saque", valor, descricao))

    def registrar_transferencia_enviada(self, valor: float, conta_destino: str) -> None:
        if valor <= 0:
            raise ValorInvalidoError("O valor da transferência deve ser maior que zero.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar a transferência.")
        self.saldo -= valor
        self.transacoes.append(
            Transacao("transferencia_enviada", valor, f"Transferência para conta {conta_destino}")
        )

    def registrar_transferencia_recebida(self, valor: float, conta_origem: str) -> None:
        self.saldo += valor
        self.transacoes.append(
            Transacao("transferencia_recebida", valor, f"Transferência da conta {conta_origem}")
        )

    def to_dict(self) -> dict:
        return {
            "numero": self.numero,
            "cliente": self.cliente.to_dict(),
            "saldo": self.saldo,
            "transacoes": [t.to_dict() for t in self.transacoes],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Conta":
        cliente = Cliente.from_dict(data.get("cliente", {}))
        transacoes = [Transacao.from_dict(t) for t in data.get("transacoes", [])]
        return cls(
            numero=data.get("numero", ""),
            cliente=cliente,
            saldo=data.get("saldo", 0.0),
            transacoes=transacoes,
        )

    def __str__(self) -> str:
        return f"Conta {self.numero} - {self.cliente.nome} - Saldo: R$ {self.saldo:.2f}"
