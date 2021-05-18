
import os
import sqlite3

dbName = "Turmas.db"

global conn
conn = sqlite3.connect(dbName)

def insert_aluno(lista_aluno):

    print("BD Aluno-Numero : ",lista_aluno[0])
    print("BD Aluno-Nome : ",lista_aluno[1])

    sql = """INSERT INTO aluno(id_aluno, Nome_Aluno, Morada_Aluno, CC_Aluno, Idade_Aluno)
          VALUES (?,?,"",0,0);
          """
    c = conn.cursor()

    dados = (lista_aluno[0], lista_aluno[1])
    c.execute(sql, dados)

    conn.commit()







