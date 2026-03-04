## 🎵 Darkmoon Records — Sistema de Catálogo de Álbuns ou CDs!

Sistema criado em python para gerenciamento de um catálogo de álbuns, com controle de estoque, avaliação de usuários e persistência de dados, com SQLite e SQLAlchemy.

Exercício prático, consolidando conhecimentos em:

• Python orientado a objetos
• Validação de inputs (CLI)
• Persistência de dados
• ORM (SCLAlchemy)
• Table relationship

## ORM

O projeto utiliza SQLAlchemy, mapeando as classes diretamente para as tabelas do banco.

| Classe Python | Tabela SQL |
| ------------- | ---------- |
| `AlbumDB`     | `albums`   |
| `RatingDB`    | `ratings`  |


## Estrutura do Projeto:

darkmoon-records/
│
├── app.py
│
├── modelo/
│   ├── darkmoon.py
│   ├── rating.py
│   └── database.py
│
├── darkmoon_records.db
│
└── README.md

## ⚙ Tecnologias:

Python 3
SQLAlchemy
SQLite