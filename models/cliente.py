class Cliente:
    """Representa um cliente do banco."""

    def __init__(self, nome: str, cpf: str, email: str = "", telefone: str = ""):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    def to_dict(self) -> dict:
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Cliente":
        return cls(
            nome=data.get("nome", ""),
            cpf=data.get("cpf", ""),
            email=data.get("email", ""),
            telefone=data.get("telefone", ""),
        )

    def __str__(self) -> str:
        return f"{self.nome} (CPF: {self.cpf})"
