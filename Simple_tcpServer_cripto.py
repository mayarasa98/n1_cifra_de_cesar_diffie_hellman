from socket import *
 
serverPort = 1300
deslocamento = 3  # mesmo valor do cliente
 
def cifra_cesar_criptografar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)
        else:
            resultado += char
    return resultado
 
def cifra_cesar_decriptografar(texto, deslocamento):
    return cifra_cesar_criptografar(texto, -deslocamento)
 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("TCP Server\n")
 
connectionSocket, addr = serverSocket.accept()
sentence = connectionSocket.recv(65000)
received = str(sentence, "utf-8")
 
# decriptografa a mensagem recebida
decrypted = cifra_cesar_decriptografar(received, deslocamento)
print("Received From Client (decrypted):", decrypted)
 
# processa e envia de volta criptografado
capitalizedSentence = decrypted.upper()
encrypted = cifra_cesar_criptografar(capitalizedSentence, deslocamento)
connectionSocket.send(bytes(encrypted, "utf-8"))
 
print("Sent back to Client (encrypted):", encrypted)
connectionSocket.close()