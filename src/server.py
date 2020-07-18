import socket

def host():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('0.0.0.0', 8080))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        resp = ''
        while True:
            data = conn.recv(4096)
            if not data:
                break
            resp += data
            print(resp)
            conn.send("Message from server")
        conn.close()
        print("Client disconnected")

if __name__=="__main__":
    host()
