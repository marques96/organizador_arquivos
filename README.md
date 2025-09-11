# 📂 Organizador de Arquivos em Python

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Ativo-success)
![Contribuições](https://img.shields.io/badge/Contribuições-Bem%20vindas-brightgreen)

Um script em **Python** para organizar automaticamente os arquivos de uma pasta, movendo-os para subpastas de acordo com suas extensões ou categorias definidas em um arquivo de configuração.  

✨ Ideal para manter pastas como **Downloads** sempre limpas e organizadas!  

---

## 🚀 Funcionalidades

✅ Organiza arquivos automaticamente por **tipo/ extensão**  
✅ Cria subpastas automaticamente, se ainda não existirem  
✅ Possui um **arquivo de configuração (`config.json`)** personalizável  
✅ Dois modos de execução:  
   - 🔹 **Manual** → organiza uma vez  
   - 🔹 **Monitoramento em tempo real** → organiza automaticamente sempre que novos arquivos aparecem  
✅ Gera um arquivo de **log (`logs/app.log`)** com todas as movimentações  
✅ Estrutura modular e orientada a objetos (**POO**)  

---

## 🛠️ Tecnologias Utilizadas

- 🐍 [Python 3.10+](https://www.python.org/)  
- 👀 [watchdog](https://pypi.org/project/watchdog/) → monitoramento em tempo real  
- 📦 `os`, `shutil`, `logging`, `argparse`, `json` (bibliotecas padrão do Python)  

---

## 📂 Estrutura do Projeto

```bash
organizador_arquivos/
│── main.py                 # Ponto de entrada
│── config.json             # Arquivo de configuração
│── requirements.txt        # Dependências do projeto
│── README.md               # Documentação
│
├── organizador/
│   ├── __init__.py
│   ├── core.py             # Lógica principal
│   ├── watcher.py          # Monitoramento em tempo real
│   ├── utils.py            # Funções auxiliares
│
├── logs/
│   └── app.log             # Arquivo de log
│
└── tests/
    └── test_core.py        # Testes unitários
