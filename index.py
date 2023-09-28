import sqlite3 as conector
import comandos

print("Testando Banco de Dados SQLite 3")

conexao = conector.connect("db-SQL3.db")

cursor = conexao.cursor()

comando = '''SELECT * FROM CARROS'''

registros = cursor.fetchall()


cursor.close()
conexao.close()
