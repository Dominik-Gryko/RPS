class RPS_Engine:
    
    def __init__(self, player_choice = None, choices = ["rock", "paper", "scissors"]):
        self.choices = choices
        self.player_choice = player_choice
        self.bot_choice = None

        if self.bot_choice == None:
            self.randomise_bot_choice()
        if self.player_choice == None:
            self.get_player_choice()
    
    
    def get_choices(self):
        return self.choices

    def get_player_choice(self):
        formatted_choices = ", ".join(self.choices)

        while True:
            print(f"The choices are: {formatted_choices}")
            player_choice = input("Enter your choice: ").lower()
            
            if player_choice in self.choices:
                self.player_choice = player_choice
                break
            else:
                print("ERROR: Invalid Choice, try again.")

    def randomise_bot_choice(self):
        import random
        self.bot_choice = self.choices[random.randint(0, 2)]
    
    def logic_OUTPUT(self, player_choice = None, bot_choice = None):
        if player_choice == None:
            player_choice = self.player_choice
        if bot_choice == None:
            bot_choice = self.bot_choice

        if player_choice == "paper":
            if bot_choice == "rock":
                print(f"OUTCOME: PLAYER WINS. Player: {player_choice}, Bot: {bot_choice}")
            if bot_choice == "scissors":
                print(f"OUTCOME: BOT WINS. Player: {player_choice}, Bot: {bot_choice}")
            if bot_choice == "paper":
                print(f"OUTCOME: DRAW. Player: {player_choice}, Bot: {bot_choice}")

        if player_choice == "rock":
            if bot_choice == "scissors":
                print(f"OUTCOME: PLAYER WINS. Player: {player_choice}, Bot: {bot_choice}")
            if bot_choice == "paper":
                print(f"OUTCOME: BOT WINS. Player: {player_choice}, Bot: {bot_choice}")
            if bot_choice == "rock":
                print(f"OUTCOME: DRAW. Player: {player_choice}, Bot: {bot_choice}")

        if player_choice == "scissors":
            if bot_choice == "paper":
                print(f"OUTCOME: PLAYER WINS. Player: {player_choice}, Bot: {bot_choice}")
            if bot_choice == "rock":
                print(f"OUTCOME: BOT WINS. Player: {player_choice}, Bot: {bot_choice}")
            if bot_choice == "scissors":
                print(f"OUTCOME: DRAW. Player: {player_choice}, Bot: {bot_choice}")
    
    def logic_BOOL(self, player_choice = None, bot_choice = None): #TRUE == Player Wins | FALSE == Bot wins | NONE == DRAW. Used to program your own output logic/statements.
        if player_choice == None:
            player_choice = self.player_choice
        if bot_choice == None:
            bot_choice = self.bot_choice

        if player_choice == "paper":
            if bot_choice == "rock":
                return True
            if bot_choice == "scissors":
                return False
            if bot_choice == "paper":
                return None

        if player_choice == "rock":
            if bot_choice == "scissors":
                return True
            if bot_choice == "paper":
                return False
            if bot_choice == "rock":
                return None

        if player_choice == "scissors":
            if bot_choice == "paper":
                return True
            if bot_choice == "rock":
                return False
            if bot_choice == "scissors":
                return None

    def start(self): #Only use this if you dont use your own interface to get the players choice. As this will get the players choice again.
        self.get_player_choice()
        self.logic_OUTPUT()