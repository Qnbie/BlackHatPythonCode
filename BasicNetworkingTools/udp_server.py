import socket
import threading

IP = "0.0.0.0"
PORT = 9997

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((IP, PORT))
    print(f'[*] UDP server listening on {IP}:{PORT}')
    while True:
        client_message = server.recvfrom(1024)
        print(f'[*] Accepted connection from {client_message[1]}')
        print(f'[*] Message: {client_message[0]}')
        server.sendto(b'ACK', client_message[1])

if __name__ == '__main__':
    main()