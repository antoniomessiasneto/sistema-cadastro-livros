
# 📚 Sistema de Cadastro de Livros

Este projeto é uma aplicação web simples desenvolvida em **Python (Django)** com persistência em **banco de dados relacional (SQLite3)**. A aplicação implementa um sistema **CRUD completo** (Create, Read, Update, Delete) para o gerenciamento de livros, com uma interface gráfica intuitiva e moderna construída com **HTML, Bootstrap 5 e CSS**.

---

## ✅ Funcionalidades CRUD

| Função  | Descrição                                                                 |
|---------|---------------------------------------------------------------------------|
| Create  | Cadastrar novos livros via formulário com campos para título, autor, ano, gênero e quantidade. |
| Read    | Listar todos os livros cadastrados em uma tabela responsiva com informações completas. |
| Update  | Editar dados diretamente na tabela (inline) e atualizar com botão.        |
| Delete  | Remover um livro da base de dados com botão "Excluir".                    |

---

## 💻 Tecnologias Utilizadas

### Linguagem:
- **Python 3.11**

### Frameworks/Bibliotecas:
- **Django 5.x**
- **Bootstrap 5 (via CDN)**
- **HTML5, CSS3**
- **Google Fonts (Poppins, Roboto)**

### Banco de Dados:
- **SQLite3** (padrão do Django)

---

## 🛠️ Como Executar a Aplicação

### Pré-requisitos:
- Python 3 instalado
- Git (opcional, para clonar o projeto)

### Passo a passo:

```bash
# 1. Clone o repositório (ou baixe o código)
git clone https://github.com/seuusuario/sistema-cadastro-livros.git
cd sistema-cadastro-livros

# 2. Crie e ative um ambiente virtual (opcional, mas recomendado) (Opcional) 
# Recomendado para evitar conflitos de dependências com outros projetos
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Instale as dependências
pip install django

# 4. Execute as migrações do banco
python manage.py migrate

# 5. Inicie o servidor
python manage.py runserver
```

Acesse no navegador: `http://127.0.0.1:8000/`

---

## 🔍 Como Testar as Funcionalidades

### Criar (Create):
1. Clique em “+ Novo Livro”.
2. Preencha os dados no formulário.
3. Clique em “Cadastrar Livro”.
4. O novo livro aparecerá na lista.

### Listar (Read):
- Todos os livros cadastrados são exibidos automaticamente em uma tabela estilizada.
- Também são exibidas estatísticas: total de livros, autores únicos e gêneros únicos.

### Atualizar (Update):
1. Altere qualquer campo diretamente na linha da tabela.
2. Clique em “Atualizar”.
3. Os dados serão salvos e a página recarregará.

### Deletar (Delete):
- Clique no botão “Excluir” na linha correspondente ao livro que deseja remover.


## 🧠 Organização do Projeto

- `models.py` – define as tabelas: Livro, Autor e Gênero.
- `views.py` – contém as regras de negócio e lógicas CRUD.
- `urls.py` – mapeia as rotas para cada funcionalidade.
- `home.html` – template principal da interface.
- `static/` e `templates/` – recursos visuais.

---

## 🧪 Validações Implementadas

- Todos os campos são obrigatórios.
- Quantidade de estoque não pode ser negativa.
- Autor e Gênero são criados automaticamente caso ainda não existam (evita duplicação textual).

---

## 📁 Estrutura de Diretórios (resumo)

```
sistema-cadastro-livros/
│
├── app_cad_livro/
│   ├── migrations/
│   ├── templates/Usuario/home.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── sistema_cadastro_livros/
│   └── settings.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔁 Versionamento

Este projeto utiliza **Git** para controle de versão. Recomendado:
```bash
git init
git add .
git commit -m "Versão inicial do sistema de cadastro de livros"
```

---

## 📌 Observações Finais

- A interface gráfica foi desenvolvida para facilitar o uso e a avaliação das funcionalidades CRUD.
- O foco foi a **clareza do código**, **boas práticas**, **reuso** e **lógica limpa**.
