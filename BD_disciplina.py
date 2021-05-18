
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

    print("Selecciona os dados da tabela disciplina")

    sql = """SELECT * FROM disciplina;"""
    c = conn.cursor()
    c.execute(sql)
    
    conn.commit()






