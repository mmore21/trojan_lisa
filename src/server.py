import socket

class Server:
    def __init__(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Server that opens a TCP socket. """
    def host(self):
        self.serv.bind((socket.INADDR_ANY, 8080))
        self.serv.listen()
        while True:
            conn, addr = self.serv.accept()
            while True:
                try:
                    data = conn.recv(4096)
                    if not data:
                        break
                    resp = data.decode()
                    print(resp)
                    self.execute(resp)
                    message = "Message from server"
                    conn.send(message.encode())
                except:
                    break
            conn.close()
            print("Client disconnected")

    def execute(self, command):
        if command == "1":
            print("Example command")


if __name__=="__main__":
    server = Server()
    server.host()