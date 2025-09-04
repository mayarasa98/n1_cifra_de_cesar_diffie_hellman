import socket
import random

def main():
    serverName = "10.1.70.35"  # IP do servidor
    serverPort = 1300

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((serverName, serverPort))
        s.listen()
        print(f"Servidor ouvindo em {serverName}:{serverPort}...")

        conn, addr = s.accept()
        with conn:
            print(f"Cliente conectado: {addr}")

            # Recebe p, g, A do cliente
            data = conn.recv(1024).decode()
            p_str, g_str, A_str = data.split(',')
            p = int(p_str)
            g = int(g_str)
            A = int(A_str)

            print(f"Servidor recebeu p={p}, g={g}, A={A} do cliente.")

            # Gera segredo e chave pública do servidor
            b = random.randint(2, p - 2)
            B = pow(g, b, p)

            # Envia B de volta ao cliente
            conn.sendall(str(B).encode())
            print(f"Servidor enviou B = {B} ao cliente.")

            # Calcula chave secreta
            secret_key = pow(A, b, p)
            print(f"✅ Servidor calculou a chave secreta: {secret_key}")

if __name__ == "__main__":
    main()
