# Cliente
import socket

class mysocket:

    def _init_(self)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "192.168.1.125"
        porto = 5525
        server_address=(host,porto)

    def connet(self, server_address)
        s.connect(server_address)

    def mysend(self, msg)
        totalsent = 0
        while totalsent < MSGLEN:
            set = s.send(msg[totalsent:])
            if sent == 0:
                print ("Erro no envio da mensagem ao servidor")
            totalsent = totalsent + sent

    def myreceive(self,msg)
        totalrecv = 0
        while totalrecv < MSGLEN:
            msg = s.recv(2048)
            if msg == b'':
                print ("Erro na recepção da mensagem do servidor")
            totalrecv = totalrecv + len(msg)

    










