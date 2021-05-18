
# Componente Servidor - MAIN

#importa o modulo com funções da tabela disciplina
import BD_disciplina
#importa o modulo com funções da tabela aluno
import BD_aluno
#importa o modulo com funções da tabela professor
import BD_professor
#importa o modulo com funções da tabela associa_aluno_disciplina
import BD_associa_aluno
#importa o modulo com funções da tabela associa_professor
import BD_associa_professor


#Estabelece a conexão Socket
import socket
print("Arranque de servidor")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# lê do ficheiro de configuração o IP do servidor
f = open("conexao_server_conf.txt", "r")
for linha in f:
    valores= linha.split()
    ip = valores[0]
f.close()
porto = 50000
server_address =(ip,porto)
s.bind(server_address)

#o Servidor fica à esculta de receber mensagens
s.listen()
print("Servidor à escuta")

#o servidor aceita a conexão
c, addr = s.accept()
print("Servidor conectado com",addr)



#Recebe as mensagens
while True:
    msg = c.recv(1024)
    if not msg:
            print("vou fechar a conexão")
            c.close()
            break
    #START - Acede às tabelas e carrega as listas
 #   if msg.decode() == 'start':
 #       select_disciplina()
 #       select_aluno()
 #       select_professor()
 #       select_associa_aluno()
 #       select_associa_professor()
        
    
    #Opção 1 - Criar Disciplina
    if msg.decode() == '1':
        print("Opção1-Criar Disciplina")
        msg = c.recv(1024)
        BD_disciplina.insert_disciplina(msg.decode())
        
    #Opção 4 - Criar Aluno
    elif msg.decode() == '4':
        print("Opção4-Criar Aluno")
        msg = c.recv(1024)
        msg =eval(msg)
        BD_aluno.insert_aluno(msg)
        
    #Opção 5 - Inscrever Aluno
    elif msg.decode() == '5':
        print("Opção5-Inscrever Aluno")
        msg = c.recv(1024)
        msg =eval(msg)
        BD_associa_aluno.insert_associa_aluno(msg)

      
    #Opção 9 - Criar Professor
    elif msg.decode() == '9':
        print("Opção9-Criar Professor")
        msg = c.recv(1024)
        msg =eval(msg)
        BD_professor.insert_professor(msg)

    #Opção 10 - Associa Professor
    elif msg.decode() == '10':
        print("Opção10-Associa Professor")
        msg = c.recv(1024)
        msg =eval(msg)
        BD_associa_professor.insert_associa_professor(msg)        
        
        
            
    
