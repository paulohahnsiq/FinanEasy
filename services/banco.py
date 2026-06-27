import json
import os

from models.cliente import Cliente
from models.conta import Conta


class ContaNaoEncontradaError(Exception):
    """Levantada quando uma conta não é encontrada pelo número informado."""


class Banco:
    """Gerencia todas as contas do banco e a persistência dos dados em JSON."""

    def __init__(self, caminho_dados: str = "data/contas.json"):
        self.caminho_dados = caminho_dados
        self.contas: dict[str, Conta] = {}
        self._proximo_numero = 1
        self.carregar_dados()

    # ---------- Persistência ----------

    def carregar_dados(self) -> None:
        pasta = os.path.dirname(self.caminho_dados)
        if pasta:
            os.makedirs(pasta, exist_ok=True)

        if not os.path.exists(self.caminho_dados):
            return

        with open(self.caminho_dados, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo:
                return
            dados = json.loads(conteudo)

        for numero, conta_dict in dados.items():
            self.contas[numero] = Conta.from_dict(conta_dict)

        if self.contas:
            self._proximo_numero = max(int(n) for n in self.contas.keys()) + 1

    def salvar_dados(self) -> None:
        pasta = os.path.dirname(self.caminho_dados)
        if pasta:
            os.makedirs(pasta, exist_ok=True)

        dados = {numero: conta.to_dict() for numero, conta in self.contas.items()}
        with open(self.caminho_dados, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    # ---------- Operações ----------

    def criar_conta(self, nome: str, cpf: str, email: str = "", telefone: str = "") -> Conta:
        numero = str(self._proximo_numero).zfill(4)
        cliente = Cliente(nome, cpf, email, telefone)
        conta = Conta(numero, cliente)
        self.contas[numero] = conta
        self._proximo_numero += 1
        self.salvar_dados()
        return conta

    def buscar_conta(self, numero: str) -> Conta:
        conta = self.contas.get(numero)
        if conta is None:
            raise ContaNaoEncontradaError(f"Conta {numero} não encontrada.")
        return conta

    def depositar(self, numero: str, valor: float) -> Conta:
        conta = self.buscar_conta(numero)
        conta.depositar(valor)
        self.salvar_dados()
        return conta

    def sacar(self, numero: str, valor: float) -> Conta:
        conta = self.buscar_conta(numero)
        conta.sacar(valor)
        self.salvar_dados()
        return conta

    def transferir(self, numero_origem: str, numero_destino: str, valor: float):
        origem = self.buscar_conta(numero_origem)
        destino = self.buscar_conta(numero_destino)

        origem.registrar_transferencia_enviada(valor, numero_destino)
        destino.registrar_transferencia_recebida(valor, numero_origem)

        self.salvar_dados()
        return origem, destino

    def listar_contas(self) -> list:
        return list(self.contas.values())
