import sys
import socket

from datetime import datetime

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 9999

user = 'black@920'


def connectserver():
    try:
        client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        print(f'[{datetime.now()}]Connecting to Server...')
        client.connect((SERVER_IP, PORT))
        print(f'[{datetime.now()}]Connected to {SERVER_IP} ON {PORT}')
        while True:
            msg_to_send = input(f'{user}> ')
            if msg_to_send == quit or len(msg_to_send) <= 0:
                client.close()
                sys.exit(1)
            else:
                msg_to_send += f'  [{datetime.now()}]'
                client.send(msg_to_send.encode())
                print('SENT')

                data_recieved = client.recv(1024).decode()
                if (len(data_recieved) > 0):
                    print('RECIEVED')
                    print(f'{SERVER_IP}: {data_recieved}')
                else:
                    client.close()
                    sys.exit(1)
    except KeyboardInterrupt:
        print('CLOSING CLIENT...')
        sys.exit(1)
    except socket.error as err:
        print(f'Client couldn\'t connect to Server: {err}')
        sys.exit(1)


connectserver()
