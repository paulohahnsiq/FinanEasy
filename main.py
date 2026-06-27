import os
import sys

from models.conta import SaldoInsuficienteError, ValorInvalidoError
from services.banco import Banco, ContaNaoEncontradaError
from services.relatorio import gerar_extrato_excel, gerar_extrato_pdf


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def ler_float(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("⚠️  Valor inválido. Digite um número (ex: 100.50).")


def exibir_menu():
    print("=" * 42)
    print("            🏦  BANCO PY")
    print("=" * 42)
    print("1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Transferir")
    print("5 - Ver extrato")
    print("6 - Exportar extrato (PDF)")
    print("7 - Exportar extrato (Excel)")
    print("8 - Listar contas")
    print("0 - Sair")
    print("=" * 42)


def criar_conta(banco: Banco):
    print("\n--- Criar Conta ---")
    nome = input("Nome do cliente: ").strip()
    cpf = input("CPF: ").strip()
    email = input("E-mail (opcional): ").strip()
    telefone = input("Telefone (opcional): ").strip()
    conta = banco.criar_conta(nome, cpf, email, telefone)
    print(f"\n✅ Conta criada com sucesso! Número da conta: {conta.numero}")


def depositar(banco: Banco):
    print("\n--- Depositar ---")
    numero = input("Número da conta: ").strip()
    try:
        valor = ler_float("Valor do depósito: R$ ")
        conta = banco.depositar(numero, valor)
        print(f"\n✅ Depósito realizado! Saldo atual: R$ {conta.saldo:.2f}")
    except (ContaNaoEncontradaError, ValorInvalidoError) as erro:
        print(f"\n❌ Erro: {erro}")


def sacar(banco: Banco):
    print("\n--- Sacar ---")
    numero = input("Número da conta: ").strip()
    try:
        valor = ler_float("Valor do saque: R$ ")
        conta = banco.sacar(numero, valor)
        print(f"\n✅ Saque realizado! Saldo atual: R$ {conta.saldo:.2f}")
    except (ContaNaoEncontradaError, ValorInvalidoError, SaldoInsuficienteError) as erro:
        print(f"\n❌ Erro: {erro}")


def transferir(banco: Banco):
    print("\n--- Transferir ---")
    origem = input("Número da conta de origem: ").strip()
    destino = input("Número da conta de destino: ").strip()
    try:
        valor = ler_float("Valor da transferência: R$ ")
        conta_origem, _ = banco.transferir(origem, destino, valor)
        print(f"\n✅ Transferência realizada! Saldo atual (origem): R$ {conta_origem.saldo:.2f}")
    except (ContaNaoEncontradaError, ValorInvalidoError, SaldoInsuficienteError) as erro:
        print(f"\n❌ Erro: {erro}")


def ver_extrato(banco: Banco):
    print("\n--- Extrato ---")
    numero = input("Número da conta: ").strip()
    try:
        conta = banco.buscar_conta(numero)
        print(f"\nConta {conta.numero} - {conta.cliente.nome}")
        print(f"Saldo atual: R$ {conta.saldo:.2f}\n")
        if not conta.transacoes:
            print("Nenhuma transação registrada ainda.")
        for transacao in conta.transacoes:
            print(transacao)
    except ContaNaoEncontradaError as erro:
        print(f"\n❌ Erro: {erro}")


def exportar_pdf(banco: Banco):
    print("\n--- Exportar extrato em PDF ---")
    numero = input("Número da conta: ").strip()
    try:
        conta = banco.buscar_conta(numero)
        caminho = gerar_extrato_pdf(conta)
        print(f"\n✅ Extrato exportado em: {caminho}")
    except ContaNaoEncontradaError as erro:
        print(f"\n❌ Erro: {erro}")


def exportar_excel(banco: Banco):
    print("\n--- Exportar extrato em Excel ---")
    numero = input("Número da conta: ").strip()
    try:
        conta = banco.buscar_conta(numero)
        caminho = gerar_extrato_excel(conta)
        print(f"\n✅ Extrato exportado em: {caminho}")
    except ContaNaoEncontradaError as erro:
        print(f"\n❌ Erro: {erro}")


def listar_contas(banco: Banco):
    print("\n--- Contas cadastradas ---")
    contas = banco.listar_contas()
    if not contas:
        print("Nenhuma conta cadastrada ainda.")
        return
    for conta in contas:
        print(conta)


def main():
    banco = Banco()

    acoes = {
        "1": criar_conta,
        "2": depositar,
        "3": sacar,
        "4": transferir,
        "5": ver_extrato,
        "6": exportar_pdf,
        "7": exportar_excel,
        "8": listar_contas,
    }

    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\n👋 Saindo do Banco Py... Até logo!")
            sys.exit(0)

        acao = acoes.get(opcao)
        if acao:
            acao(banco)
        else:
            print("\n⚠️  Opção inválida.")

        pausar()


if __name__ == "__main__":
    main()
