# backend/populate_db.py
from models import User, session

# Dados de exemplo para popular o banco de dados
users = [
    User(name='Alice', age=30),
    User(name='Bob', age=24),
    User(name='Charlie', age=29)
]

# Adiciona os dados ao banco de dados
session.add_all(users)
session.commit()
session.close()
print("Banco de dados populado com sucesso!")
