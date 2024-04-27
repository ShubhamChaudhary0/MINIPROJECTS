
def rock_paper_scissor():
    print("THE GAME BEGINS--:>")
    player1 = input("ENTER PLAYER1 NAME: ")
    player2 = input("ENTER PLAYER2 NAME: ")
    import random
    if player2=="bot":
        play1 = input("ENTER YOUR CHOICE[ROCK/PAPER/SCISSOR]: ")
        play2 = random.choice(["ROCK","PAPER","SCISSOR"])
        print(play1,play2)
        if play1 == "ROCK" and play2 == "PAPER":
         print(f"{player2} HAS WON!!")
        elif play1 == "PAPER" and play2 == "ROCK":
         print(f"{player1} HAS WON!!")
        elif play2 == "SCISSOR" and play1 == "PAPER":
         print(f"{player2} HAS WON!!")
        elif play1 == "SCISSOR" and play2 == "PAPER":
         print(f"{player1} HAS WON!!")
        elif play1 == "ROCK" and play2 == "SCISSOR":
         print(f"{player1} HAS WON!!")
        elif play2 == "ROCK" and play1 == "SCISSOR":
         print(f"{player2} HAS WON!!")
        else:
         print("ITS A TIE!!")
    else:
      play1 = input("ENTER YOUR CHOICE[ROCK/PAPER/SCISSOR]: ")
      play2 = input("ENTER YOUR CHOICE[ROCK/PAPER/SCISSOR]: ")
      print(play1,play2)
      if play1 == "ROCK" and play2 == "PAPER":
        print(f"{player2} HAS WON!!")
      elif play1 == "PAPER" and play2 == "ROCK":
        print(f"{player1} HAS WON!!")
      elif play2 == "SCISSOR" and play1 == "PAPER":
        print(f"{player2} HAS WON!!")
      elif play1 == "SCISSOR" and play2 == "PAPER":
         print(f"{player1} HAS WON!!")
      elif play1 == "ROCK" and play2 == "SCISSOR":
        print(f"{player1} HAS WON!!")
      elif play2 == "ROCK" and play1 == "SCISSOR":
        print(f"{player2} HAS WON!!")
      else:
        print("ITS A TIE!!")
rock_paper_scissor()


    
    
    