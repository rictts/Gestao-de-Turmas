
import os
import sqlite3

dbName = "Turmas.db"

global conn
conn = sqlite3.connect(dbName)

def insert_professor(lista_professor):

    print("BD Professor-Numero : ",lista_professor[0])
    print("BD Professor-Nome : ",lista_professor[1])

    sql = """INSERT INTO professor(id_professor, Nome_Professor, Morada_Professor, Idade_Professor, Categoria_Profissional, Anos_Experiencia)
          VALUES (?,?,"",0,"",0);
          """
    c = conn.cursor()

    dados = (lista_professor[0], lista_professor[1])
    c.execute(sql, dados)

    conn.commit()

def select_professor():

    lista_professor = list()
    print("BD Professor-Select ")

    sql = """SELECT * from professor;"""
    c = conn.cursor()
    resultado = c.execute(sql)
    for linha in resultado:
        lista_professor.append(linha)
    return lista_professor





