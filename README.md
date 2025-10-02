# API.AP1.Monolitica

Projeto de AP1 para a matéria de Desenvolvimento de API.

## Sumário

- [Sobre](#sobre)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Endpoints Principais](#endpoints-principais)
- [Contribuição](#contribuição)
- [Requisitos](#requsitos)

## Sobre

API monolítica desenvolvida como uma forma de avaliação AP1. O objetivo é praticar conceitos de desenvolvimento de APIs RESTful utilizando Python

## ✨ Principais Funcionalidades

- 🔗 API RESTful monolítica
- 🐍 Desenvolvida em Python
- 📚 Gerenciamento de alunos, professores e turmas
- 🚀 Fácil execução e configuração
- 🛠️ Estrutura organizada para facilitar manutenção

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/ImpactaHumbertoFilho/API.AP1.Monolitica>
   cd API.AP1.Monolitica
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

Execute o aplicativo de uma das formas abaixo:

- Usando o arquivo `run.py` (recomendado):
  ```bash
  python run.py
  ```
- Ou diretamente como módulo Python:
  ```bash
  python -m src.main
  ```

O servidor será iniciado em `http://localhost:5000`.

## Estrutura do Projeto

```
API.AP1.Monolitica/
├── src/
│   └── config/
        └── __init__.py
        └── base.py
    └── controllers/
        └── aluno_controller.py
        └── professor_controller.py
        └── turma_controller.py
    └── models/
        └── __init__.py
        └── main.py
    └── main.py
├── .gitignore
├── LICENSE
├── meu_banco.db
├── README.md
├── requirements.txt
└── run.py
```

## Endpoints Principais
        # GET    /professor/<int:id>   -> get_professor
        # POST   /professor/           -> create_professor
        # PUT    /professor/<int:id>   -> update_professor
        # DELETE /professor/<int:id>   -> delete_professor
        # GET    /turma/           -> get_turmas
        # GET    /turma/<int:id>   -> get_turma
        # POST   /turma/           -> create_turma
        # PUT    /turma/<int:id>   -> update_turma
        # DELETE /turma/<int:id>   -> delete_turma
        # GET /aluno/              -> get_alunos

## Contribuição

Features e commits dos alunos envolvidos.

## Requisitos

- Python 3.10 ou superior
- Instale o [Python](https://www.python.org/downloads/) na versão 3.10 ou superior.
- Certifique-se de ter o [pip](https://pip.pypa.io/en/stable/installation/) instalado para gerenciar dependências.
- Recomenda-se utilizar um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
- Após instalar as dependências, execute os testes (se houver) para garantir que tudo está funcionando:
    ```bash
    pytest
    ```