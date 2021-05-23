
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
    c.close()

def select_associa_aluno():

    lista_associa_aluno = list()
    print("BD Associa Aluno-Select ")

    sql = """SELECT * from associa_aluno_disciplina;"""
    c = conn.cursor()
    resultado = c.execute(sql)
    for linha in resultado:
        lista_associa_aluno.append(linha)
    return lista_associa_aluno

def delete_associa_aluno(aluno):

    print("Apaga na Base de dados:",aluno)

    sql = """DELETE FROM associa_aluno_disciplina WHERE id_aluno = ?;"""
    c = conn.cursor()

    dados = (aluno)
    c.execute(sql, (dados,))

    conn.commit()

def delete_associa_aluno_disciplina(disciplina):

    print("Apaga na Base de dados:",disciplina)

    sql = """DELETE FROM associa_aluno_disciplina WHERE Nome_Disciplina = ?;"""
    c = conn.cursor()

    dados = (disciplina)
    c.execute(sql, (dados,))

    conn.commit()

