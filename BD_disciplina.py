
import os
import sqlite3

dbName = "Turmas.db"

global conn
conn = sqlite3.connect(dbName)

def insert_disciplina(disciplina):

    print("Insere na Base de dados:",disciplina)

    sql = """INSERT INTO disciplina(Nome_Disciplina) VALUES (?);"""
    c = conn.cursor()

    dados = (disciplina)
    c.execute(sql, (dados,))

    conn.commit()

def select_disciplina():

    lista_disciplina = list()
    print("BD Disciplina-Select ")

    sql = """SELECT * from disciplina;"""
    c = conn.cursor()
    resultado = c.execute(sql)
    for linha in resultado:
        lista_disciplina.append(linha)
    return lista_disciplina

def delete_disciplina(disciplina):

    print("Apaga na Base de dados:",disciplina)

    sql = """DELETE FROM disciplina WHERE Nome_Disciplina = ?;"""
    c = conn.cursor()

    dados = (disciplina)
    c.execute(sql, (dados,))

    conn.commit()



