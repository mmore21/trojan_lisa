import socket

class Client():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Client that connects to a remote TCP socket. """
    def connect(self):
        self.sock.connect(('0.0.0.0', 8080))
    
    def close(self):
        self.sock.close()
    
    def message(self, message):
        self.sock.send(message.encode())
        resp = self.sock.recv(4096)
        return resp.decode()

if __name__=="__main__":
    client = Client()
    client.connect()
    resp = client.message("Message from Client")
    print(resp)
    client.close()