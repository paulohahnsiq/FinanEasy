<h1 align="center">🏦 Banco Py</h1>

<p align="center">
  Sistema bancário em linha de comando (CLI) desenvolvido em Python, utilizando Programação Orientada a Objetos.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OOP-4B8BBE?style=for-the-badge" />
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/fpdf2-D32F2F?style=for-the-badge" />
  <img src="https://img.shields.io/badge/openpyxl-217346?style=for-the-badge" />
</p>

---

## 📋 Sobre o projeto

O **Banco Py** é um sistema bancário simulado, desenvolvido inteiramente em Python, que permite gerenciar contas, realizar operações financeiras e gerar relatórios de extrato em PDF e Excel. O projeto foi criado como prática de **Programação Orientada a Objetos (POO)**, manipulação de arquivos e geração de relatórios.

---

## ✨ Funcionalidades

- 👤 Criação e gerenciamento de contas (cliente/conta)
- 💰 Depósito e saque
- 🔁 Transferência entre contas
- 📜 Histórico de transações
- 📄 Exportação de extrato em **PDF** (via `fpdf2`)
- 📊 Exportação de extrato em **Excel** (via `openpyxl`)
- 💾 Persistência de dados em **JSON** (os dados não se perdem ao fechar o programa)

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Uso |
|---|---|
| **Python** | Linguagem principal do projeto |
| **POO (Orientação a Objetos)** | Estruturação das classes `Conta`, `Cliente`, `Transacao`, etc. |
| **fpdf2** | Geração de extratos em PDF |
| **openpyxl** | Geração de extratos em Excel |
| **JSON** | Persistência dos dados das contas e transações |

---

## 📂 Estrutura do projeto

```
banco-py/
├── main.py                # Ponto de entrada do sistema (menu CLI)
├── models/
│   ├── conta.py            # Classe Conta
│   ├── cliente.py          # Classe Cliente
│   └── transacao.py        # Classe Transacao
├── services/
│   ├── banco.py             # Regras de negócio (depósito, saque, transferência)
│   └── relatorio.py          # Geração de extrato em PDF/Excel
├── data/
│   └── contas.json          # Persistência dos dados
├── requirements.txt
└── README.md
```

> 📝 Ajuste essa estrutura para refletir exatamente as pastas/arquivos do seu projeto real.

---

## 🚀 Como executar

### Pré-requisitos
- Python 3.10 ou superior instalado

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/paulohahnsiq/banco-py.git

# 2. Acesse a pasta do projeto
cd banco-py

# 3. Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Execute o sistema
python main.py
```

---

## 💻 Exemplo de uso

```
=== BANCO PY ===
1 - Criar conta
2 - Depositar
3 - Sacar
4 - Transferir
5 - Ver extrato
6 - Exportar extrato (PDF/Excel)
0 - Sair

Escolha uma opção: 2
Informe o valor do depósito: 500.00
✅ Depósito realizado com sucesso! Saldo atual: R$ 500.00
```

---

## 🗺️ Próximas melhorias (roadmap)

- [ ] Autenticação por senha/PIN
- [ ] Suporte a múltiplas moedas
- [ ] Interface gráfica (GUI) ou versão web
- [ ] Testes automatizados (pytest)
- [ ] Integração com banco de dados (SQLite/MySQL) no lugar do JSON

---

## 👨‍💻 Autor

**Paulo Victor**
Estudante de Ciência da Computação | Desenvolvedor Python em formação

[GitHub](https://github.com/paulohahnsiq)

---

<p align="center"><i>Projeto desenvolvido para fins de aprendizado e portfólio. 🚀</i></p>
# banco-py
