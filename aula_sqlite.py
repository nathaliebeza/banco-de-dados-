import sqlite3
banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()
cursor.execute('CREATE TABLE IF NOT EXIST clientes (nome text, idade integer, email text )')
banco.commit()
