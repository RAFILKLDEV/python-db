import sqlite3 as conector
import comandos

print("Testando Banco de Dados SQLite 3")

conexao = conector.connect("db-SQL3.db")
cursor = conexao.cursor()

# cursor.execute(comandos.inserirPessoa)
# conexao.commit()

cursor.execute(comandos.join)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexao.close()
