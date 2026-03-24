import socket
import threading

class ChatServer:
    def __init__(self, host='127.0.0.1', port=12345):
        self.clients = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()

        print("Servidor iniciado...")

    def broadcast(self, message, client):
        for c in self.clients:
            if c != client:
                c.send(message)

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message, client)
            except:
                self.clients.remove(client)
                client.close()
                break

    def start(self):
        while True:
            client, addr = self.server.accept()
            print(f"Conectado: {addr}")
            self.clients.append(client)

            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

if __name__ == "__main__":
    ChatServer().start()