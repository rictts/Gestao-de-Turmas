
import os
import sqlite3

dbName = "Turmas.db"

global conn
conn = sqlite3.connect(dbName)

def insert_associa_aluno(lista_associa_aluno):

    print("BD associa_aluno-Numero aluno : ",lista_associa_aluno[0])
    print("BD associa_aluno-Nome disciplina: ",lista_associa_aluno[1])

    sql = """INSERT INTO associa_aluno_disciplina(id_aluno, Nome_disciplina)
          VALUES (?,?);
          """
    c = conn.cursor()

    dados = (lista_associa_aluno[0], lista_associa_aluno[1])
    c.execute(sql, dados)

    conn.commit()







