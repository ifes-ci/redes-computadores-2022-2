import socket

HOST = ""  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

LISTA_USUARIOS = []

def server():
    print(f"Starting UDP Server on port {PORT}")
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = (HOST, PORT)
    udp.bind(orig)
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode('utf-8')
        print(f"{cliente} {msg_decoded}")
        LISTA_USUARIOS.append(cliente)
        for usuario in LISTA_USUARIOS:
            udp.sendto(msg, usuario)
    udp.close()


if __name__ == "__main__":
    server()
