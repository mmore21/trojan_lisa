import socket

class Server:
    def __init__(self):
        self.commands = {
            0: "Exit from RAT interface",
            1: "Set Mona Lisa as desktop background"
        }
        self.run_rat_interface()


    def run_rat_interface(self):
        while True:
            print("Le Louvre RAT Interface")
            for command, description in self.commands:
                print(command, "->", description)
            
            command_key = input()
            # Invalid input
            if command_key not in self.commands:
                continue
            # Exit program
            elif command_key == 0:
                return
            else:
                self.execute_command(command_key)

    def execute_command(self, command_key):
        # TODO: Set background to Mona Lisa
        if command_key == 1:
            pass
        

    def host(self):
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
    server = Server()
    server.host()