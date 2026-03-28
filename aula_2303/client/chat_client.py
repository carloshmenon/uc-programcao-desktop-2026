import socket
import threading

class ChatClient:
    def __init__(self, host='10.28.2.0', port=8080):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.callbacks = []

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                for callback in self.callbacks:
                    callback(message)
            except:
                self.client.close()
                break

    def send(self, message):
        self.client.send(message.encode())

    def start(self):
        thread = threading.Thread(target=self.receive, daemon=True)
        thread.start()

    def on_message(self, callback):
        self.callbacks.append(callback)