import socket

class Client():
    def __init__(self):
        pass

    """ Client that connects to a remote TCP socket. """
    def connect(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('0.0.0.0', 8080))
        client.send("Message from client")
        resp = client.recv(4096)
        client.close()
        print(resp)

if __name__=="__main__":
   client = Client()
   client.connect()