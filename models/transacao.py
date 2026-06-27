from datetime import datetime


class Transacao:
    """Representa uma transação financeira (depósito, saque ou transferência)."""

    def __init__(self, tipo: str, valor: float, descricao: str = "", data: str = None):
        self.tipo = tipo  # deposito | saque | transferencia_enviada | transferencia_recebida
        self.valor = valor
        self.descricao = descricao
        self.data = data or datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def to_dict(self) -> dict:
        return {
            "tipo": self.tipo,
            "valor": self.valor,
            "descricao": self.descricao,
            "data": self.data,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Transacao":
        return cls(
            tipo=data.get("tipo", ""),
            valor=data.get("valor", 0.0),
            descricao=data.get("descricao", ""),
            data=data.get("data", ""),
        )

    def __str__(self) -> str:
        entradas = ("deposito", "transferencia_recebida")
        sinal = "+" if self.tipo in entradas else "-"
        tipo_formatado = self.tipo.replace("_", " ").title()
        return f"[{self.data}] {tipo_formatado:<24} {sinal}R$ {self.valor:.2f}  {self.descricao}"
