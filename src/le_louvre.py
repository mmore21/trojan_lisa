import client

class LeLouvre:
    def __init__(self):
        self.commands = {
            "0": "Exit from RAT interface",
            "1": "Replace all images with Mona Lisa",
            "2": "Revert all images back to their original state",
            "3": "Set wallpaper to Mona Lisa"
        }
        self.client = client.Client()

    """ Runs an interactive CLI RAT interface. """
    def run_rat_interface(self):
        self.client.connect()
        while True:
            print("\n" + "#" * 23 + "\nLe Louvre RAT Interface\n" + "#" * 23 + "\n") 
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
                break
            else:
                self.execute_command(command_key)

        self.client.close()

    """ Executes command based on the command key provided. """
    def execute_command(self, command_key):
        resp = self.client.message(command_key)
        print(resp)
            
if __name__=="__main__":
    le_louvre = LeLouvre()
    le_louvre.run_rat_interface()