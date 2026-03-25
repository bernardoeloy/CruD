# 🎮 Biblioteca de Jogos — API REST

API para gerenciamento de uma biblioteca de jogos, desenvolvida com **Python**, **Flask** e **SQLite**.

---

## 📋 Requisitos

- Python 3.8+
- Flask

Instale as dependências:
```bash
pip install flask
```

---

## 🗄️ Configuração do Banco de Dados

Antes de iniciar a API, crie o banco de dados executando:
```bash
python criar_banco.py
```

Isso irá gerar o arquivo `biblioteca_jogos.db` com a tabela `jogos` e 10 jogos de exemplo já inseridos.

---

## ▶️ Como Executar
```bash
python app.py
```

A API ficará disponível em: `http://localhost:5000`

---

## 📡 Endpoints

### Listar todos os jogos
`GET /jogos`
```json
[
  {
    "id": 1,
    "titulo": "The Witcher 3",
    "genero": "RPG",
    "plataforma": "PC",
    "preco": 149.90
  }
]
```

---

### Buscar jogo por ID
`GET /jogos/<id>`

**✅ 200 — Sucesso:**
```json
{
  "id": 1,
  "titulo": "The Witcher 3",
  "genero": "RPG",
  "plataforma": "PC",
  "preco": 149.90
}
```

**❌ 404 — Não encontrado:**
```json
{ "erro": "Jogo não encontrado" }
```

---

### Cadastrar novo jogo
`POST /jogos`

**Body:**
```json
{
  "titulo": "Cyberpunk 2077",
  "genero": "RPG",
  "plataforma": "PC",
  "preco": 129.90
}
```

**✅ 201 — Criado:**
```json
{ "mensagem": "Jogo cadastrado com sucesso!" }
```

---

### Atualizar jogo
`PUT /jogos/<id>`

**Body:**
```json
{
  "titulo": "Cyberpunk 2077",
  "genero": "RPG",
  "plataforma": "PS5",
  "preco": 99.90
}
```

**✅ 200 — Sucesso:**
```json
{ "mensagem": "Jogo atualizado com sucesso!" }
```

---

### Remover jogo
`DELETE /jogos/<id>`

**✅ 200 — Sucesso:**
```json
{ "mensagem": "Jogo 'Cyberpunk 2077' removido!" }
```

---

## 🗂️ Estrutura do Projeto
```
📁 biblioteca-jogos/
├── app.py              # API principal
├── criar_banco.py      # Script de criação do banco
├── biblioteca_jogos.db # Banco de dados (gerado automaticamente)
└── README.md
```
