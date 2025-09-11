📂 Organizador Automático de Arquivos

Um script em Python para organizar automaticamente os arquivos de uma pasta, movendo-os para subpastas de acordo com suas extensões ou categorias definidas em um arquivo de configuração.

Ideal para manter pastas como Downloads sempre limpas e organizadas.

🚀 Funcionalidades

Organiza arquivos automaticamente por tipo/ extensão.

Cria subpastas automaticamente, se ainda não existirem.

Possui um arquivo de configuração (config.json) para personalizar as regras.

Dois modos de execução:

Manual → organiza uma vez.

Monitoramento em tempo real → organiza automaticamente sempre que novos arquivos aparecem.

Gera um arquivo de log (logs/app.log) com todas as movimentações.

Estrutura modular e orientada a objetos (POO).

🛠️ Tecnologias Utilizadas

Python 3.10+

watchdog
 → para monitoramento em tempo real

os, shutil, logging, argparse, json (bibliotecas padrão do Python)

📂 Estrutura do Projeto
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

⚙️ Configuração (config.json)
{
    "rules": {
        "Documentos": [".pdf", ".docx", ".txt"],
        "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
        "Áudios": [".mp3", ".wav"],
        "Vídeos": [".mp4", ".mkv"],
        "Compactados": [".zip", ".rar"]
    },
    "default_folder": "Outros"
}

▶️ Como Usar
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/organizador_arquivos.git
cd organizador_arquivos

2️⃣ Criar ambiente virtual e instalar dependências
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3️⃣ Executar em modo manual
python main.py -p "C:/Users/SeuUsuario/Downloads"

4️⃣ Executar em modo monitoramento
python main.py -p "C:/Users/SeuUsuario/Downloads" -w

📜 Exemplo de Uso

Antes:

Downloads/
├── foto.jpg
├── documento.pdf
├── musica.mp3
├── video.mp4


Depois de executar:

Downloads/
├── Documentos/
│   └── documento.pdf
├── Imagens/
│   └── foto.jpg
├── Áudios/
│   └── musica.mp3
├── Vídeos/
│   └── video.mp4

🧪 Testes

Rodar os testes unitários:

pytest tests/

📌 Melhorias Futuras

Adicionar interface gráfica (Tkinter ou PyQt).

Suporte a mover arquivos para pastas em outros diretórios.

Compactar arquivos antigos automaticamente.

Integração com sistemas de backup.

👨‍💻 Autor
Matheus Marques

Se quiser contribuir, fique à vontade para abrir issues e pull requests.