import socket
import random

def is_prime_fast(N):
    if N <= 1:
        return False
    if N <= 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False
    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    serverName = "10.1.70.35"  # IP do servidor
    serverPort = 1300

    # Cliente escolhe p e g
    p = int(input("Cliente: Digite um número primo (p): "))
    if not is_prime_fast(p):
        print(f"{p} não é primo! Encerrando.")
        return

    g = int(input("Cliente: Digite a base geradora (g), menor que p: "))
    if g >= p:
        print("A base geradora g deve ser menor que p. Encerrando.")
        return

    # Gera segredo e chave pública do cliente
    a = random.randint(2, p - 2)
    A = pow(g, a, p)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((serverName, serverPort))
        print(f"Cliente conectado ao servidor {serverName}:{serverPort}")

        # Envia p, g e A
        msg = f"{p},{g},{A}"
        s.sendall(msg.encode())
        print(f"Cliente enviou p={p}, g={g}, A={A} ao servidor.")

        # Recebe B do servidor
        data = s.recv(1024)
        B = int(data.decode())
        print(f"Cliente recebeu B = {B} do servidor.")

        # Calcula chave secreta
        secret_key = pow(B, a, p)
        print(f"✅ Cliente calculou a chave secreta: {secret_key}")

if __name__ == "__main__":
    main()
