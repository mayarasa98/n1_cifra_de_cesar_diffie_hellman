from socket import *
serverName = "10.1.70.35"
serverPort = 1300
deslocamento = 3  # você pode escolher outro valor

# Função para criptografar usando Cifra de César
def cifra_cesar_criptografar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():  # só letras
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)
        else:
            resultado += char  # mantém números e símbolos
    return resultado

# Função para decriptografar
def cifra_cesar_decriptografar(texto, deslocamento):
    return cifra_cesar_criptografar(texto, -deslocamento)

# Conecta ao servidor
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Digita a frase, criptografa e envia
sentence = input("Input lowercase sentence: ")
encrypted = cifra_cesar_criptografar(sentence, deslocamento)
clientSocket.send(bytes(encrypted, "utf-8"))

# Recebe a resposta criptografada e decriptografa
modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence, "utf-8")
decrypted = cifra_cesar_decriptografar(text, deslocamento)

print("Received from Server (decrypted):", decrypted)

clientSocket.close()