
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

def select_associa_professor():

    lista_associa_professor = list()
    print("BD Associa Professor-Select ")

    sql = """SELECT * from associa_professor_disciplina;"""
    c = conn.cursor()
    resultado = c.execute(sql)
    for linha in resultado:
        lista_associa_professor.append(linha)
    return lista_associa_professor


def delete_associa_professor_disciplina(disciplina):

    print("Apaga na Base de dados:",disciplina)

    sql = """DELETE FROM associa_professor_disciplina WHERE Nome_Disciplina = ?;"""
    c = conn.cursor()

    dados = (disciplina)
    c.execute(sql, (dados,))

    conn.commit()



