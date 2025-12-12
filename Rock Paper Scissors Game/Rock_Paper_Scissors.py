#This app is Rock Paper Scissors Game
import random
print("Welcome to the Rock Paper Scissors Game")

class Player:
    #Parent class
    moves=["r","p","s"]
    
    def __init__(self, name="unknown" , score=0):
        self.name = name
        self.score = score

class HumanPlayer(Player):
    
    def __init__(self, name, score=0):
        super().__init__(name, score)
    
    def make_move(self):
        self.move = input("Enter your choice rock, paper, scissors => (r/p/s):")
        return self.move


class ComputerPlayer(Player):
    
    def __init__(self, score=0):
        super().__init__(score)
        self.name = "Computer player"
    
    def make_move(self):
        move=random.choice(Player.moves)
        return move

class Game():
    # this is main class of game
    rounds=0
    rounds=int(input("How many times do you want to play?: "))
    
    def play_round(self):
        H_player=HumanPlayer(input("Enter your name: "))
        C_player=ComputerPlayer()
        while True:
            H_move=H_player.make_move()
            C_move=C_player.make_move()
            print(f"{H_player.name} move is: [ {H_move} ] and {C_player.name} move is: [ {C_move} ] ")
            if H_move == C_move :
                print("Both became equal. No points are awarded.")
            
            elif H_move =="r" and C_move =="s":
                print(f"Winner this round is {H_player.name}")
                H_player.score += 1
            elif H_move =="r" and C_move =="p":
                print(f"Winner this round is {C_player.name}")
                C_player.score += 1
            elif H_move =="p" and C_move =="r":
                print(f"Winner this round is {H_player.name}")
                H_player.score += 1
            elif H_move =="p" and C_move =="s":
                print(f"Winner this round is {C_player.name}")
                C_player.score += 1
            elif H_move =="s" and C_move =="r":
                print(f"Winner this round is {C_player.name}")
                C_player.score += 1
            elif H_move =="s" and C_move =="p":
                print(f"Winner this round is {H_player.name}")
                H_player.score += 1
            print(f"score {H_player.name}: {H_player.score} and score {C_player.name}: {C_player.score}")
            print(f"{Game.rounds} times left")
            Game.rounds -=1
            if Game.rounds==0:
                break
        
        C_score=C_player.score
        H_score=H_player.score
        print(f"Human player score is {H_score} and Computer player score is {C_score}")
        if H_score>C_score:
            print(f"Winner of the game is {H_player.name}")
        elif C_score>H_score:
            print(f"Winner of the game is {C_player.name}")
        else:
            print(f" {H_player.name} and {C_player.name} Both became equal !!!")



# run the class and game
run_game=Game()
run_game.play_round()