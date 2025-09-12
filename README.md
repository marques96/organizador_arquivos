# 📂 Organizador de Arquivos em Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Watchdog](https://img.shields.io/badge/Watchdog-monitoring-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 💡 Descrição

Desenvolvi este script em Python que organiza automaticamente arquivos em pastas baseadas em suas extensões a qual utilizei um arquivo JSON para indentificar as extensões.  

Ele suporta:

- Organização manual de arquivos já existentes.  
- Monitoramento em tempo real de novos arquivos usando `watchdog`.  
- Configuração personalizada via `config.json`.  
- Tratamento de arquivos em uso no Windows, com retry e verificação de transferência concluída.  

---

## 🚀 Funcionalidades

- Organiza arquivos automaticamente por tipo/ extensão.
- Cria subpastas automaticamente, se ainda não existirem.
- Possui um arquivo de configuração (config.json) para personalizar as regras.
- Dois modos de execução:
- Manual → organiza uma vez.
- Monitoramento em tempo real → organiza automaticamente sempre que novos arquivos aparecem.
- Gera um arquivo de log (logs/app.log) com todas as movimentações.
- Estrutura modular e orientada a objetos (POO).

## ⚙️ Instalação

1️⃣ Clone o repositório:

```terminal
git clone https://github.com/marques96/organizador_arquivos
```

2️⃣ Criar o ambiente virtual e instalar dependências

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

3️⃣ Executar em modo manual
```bash
python main.py -p "C:/Users/SeuUsuario/Downloads"
```

4️⃣ Executar em modo monitoramento
```bash
python main.py -p "C:/Users/SeuUsuario/Downloads" -w
```