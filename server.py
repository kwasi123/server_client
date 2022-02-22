import sys
import socket
from datetime import datetime


SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 9999

user = 'kwasi@123'


def createserver():
    try:
        server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        print(f'[{datetime.now()}]Starting Server...')
        server.bind((SERVER_IP, PORT))
        print(f'[{datetime.now()}]Server started...')
        server.listen(10)
        print(f'[{datetime.now()}]Server Listening on {PORT}')
        connection, address = server.accept()
        print(f'SERVER Recieved a connection from {address[0]} on {address[1]}')
        while True:
            data_recieved = connection.recv(1024).decode()
            print('RECIEVED')
            if (len(data_recieved) <= 0):
                connection.close()
                break
            else:
                print(f'{address[0]}: {data_recieved}')
                msg_to_send = input(f'{user}> ')
                if msg_to_send.lower() != 'quit':
                    msg_to_send += f'  [{datetime.now()}]'
                    connection.send(msg_to_send.encode())
                    print('SENT')
                else:
                    server.close()
                    sys.exit(1)
    except KeyboardInterrupt:
        print('SHUTTING DOWN SERVER...')
        sys.exit(1)
    except socket.error as err:
        print(f'Server failed to start: {err}')
        

createserver()
