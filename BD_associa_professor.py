
import os
import sqlite3

dbName = "Turmas.db"

global conn
conn = sqlite3.connect(dbName)

def insert_associa_professor(lista_associa_professor):

    print("BD associa_professor-Numero professor : ",lista_associa_professor[0])
    print("BD associa_professor-Nome disciplina: ",lista_associa_professor[1])

    sql = """INSERT INTO associa_professor_disciplina(id_professor, Nome_disciplina)
          VALUES (?,?);
          """
    c = conn.cursor()

    dados = (lista_associa_professor[0], lista_associa_professor[1])
    c.execute(sql, dados)

    conn.commit()







