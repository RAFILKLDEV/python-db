import sqlite3 as conector
import comandos

print("Testando Banco de Dados SQLite 3")

conexao = conector.connect("db-SQL3.db")
cursor = conexao.cursor()

comando = '''--sql
    SELECT ANIME.NOME FROM ANIME INNER JOIN LISTA ON LISTA.id_lista = ANIME.id_Anime
'''
cursor.execute(comando)
registros = cursor.fetchall()
print(registros)

# conexao.commit()

cursor.close()
conexao.close()
