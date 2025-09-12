# 📂 Organizador de Arquivos

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Watchdog](https://img.shields.io/badge/Watchdog-monitoring-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 💡 Descrição

O **Organizador de Arquivos** é um script em Python que organiza automaticamente arquivos em pastas baseadas em suas extensões.  
Ele suporta:

- Organização manual de arquivos já existentes.  
- Monitoramento em tempo real de novos arquivos usando `watchdog`.  
- Configuração personalizada via `config.json`.  
- Tratamento de arquivos em uso no Windows, com retry e verificação de transferência concluída.  

---

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/organizador-arquivos.git
cd organizador-arquivos
