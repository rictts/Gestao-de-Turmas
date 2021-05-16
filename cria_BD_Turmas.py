
import os
import sqlite3

dbName = "Turmas.db"

global conn
conn = sqlite3.connect(dbName)

sql = """
CREATE TABLE aluno(
    id_aluno integer primary key  not null,
    Nome_Aluno text,
    Morada_Aluno text,
    CC_Aluno integer,
    Idade_Aluno integer);
"""
conn.executescript(sql)

sql = """
CREATE TABLE disciplina(
    Nome_Disciplina text primary key  not null);
"""
conn.executescript(sql)

sql = """
CREATE TABLE professor(
    id_professor integer primary key  not null,
    Nome_Professor text,
    Morada_Professor text,
    Idade_Professor integer,
    Categoria_Profissional text,
    Anos_Experiencia integer);
"""
conn.executescript(sql)

sql = """
CREATE TABLE associa_aluno_disciplina(
    id_aluno integer  not null,
    Nome_Disciplina text not null,
    PRIMARY KEY(id_aluno,Nome_Disciplina) );
"""
conn.executescript(sql)

sql = """
CREATE TABLE associa_professor_disciplina(
    id_professor integer not null,
    Nome_Disciplina text not null,
    PRIMARY KEY(id_professor,Nome_Disciplina) );
"""
conn.executescript(sql)

conn.commit()
