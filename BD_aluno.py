
import os
import sqlite3

dbName = "Turmas.db"

global conn
conn = sqlite3.connect(dbName)

def insert_aluno(Numero_aluno, Nome_aluno):

    print("Base de dados: ",Numero_aluno)
    print("Base de dados: ",Nome_aluno)

    sql = """INSERT INTO aluno(Numero_aluno, Nome_aluno, Morada_aluno, Idade_aluno, CC_aluno)
          VALUES (?,?,"",0,0);
          """
    c = conn.cursor()

    dados = (Numero_aluno, Nome_aluno)
    c.execute(sql, (dados,))

    conn.commit()







