Turn = "x"
play = True

bored = ["Tl", "TM", "TR", "Ml", "MM", "Mr", "bl", "bm", "br"]

def reset():
  bored = ["Tl", "TM", "TR", "Ml", "MM", "Mr", "bl", "bm", "br"]
  play = True
  turn = "x "
  print("___________________________________")
  main(turn, play, bored)

def main(Turn, play, bored):
  turn = "x "
  x = 0
  while play and x < 9:
    x += 1
    print(bored[0], bored[1], bored[2])
    print(bored[3], bored[4], bored[5])
    print(bored[6], bored[7], bored[8])
    move = input()
    if move == "tl" and bored[0] != "x " and bored[0] != "o ":
      bored[0] = Turn
    elif move == "tm" and bored[1] != "x " and bored[1] != "o ":
      bored[1] = Turn
    elif move == "tr" and bored[2] != "x " and bored[2] != "o ":
      bored[2] = Turn
    elif move == "ml" and bored[3] != "x " and bored[3] != "o ":
      bored[3] = Turn
    elif move == "mm" and bored[4] != "x " and bored[4] != "o ":
      bored[4] = Turn
    elif move == "mr" and bored[5] != "x " and bored[5] != "o ":
      bored[5] = Turn
    elif move == "bl" and bored[6] != "x " and bored[6] != "o ":
      bored[6] = Turn
    elif move == "bm" and bored[7] != "x " and bored[7] != "o ":
      bored[7] = Turn
    elif move == "br" and bored[8] != "x " and bored[8] != "o ":
      bored[8] = Turn
    else:
      turn = False
    
    if bored[0] == bored[1] == bored[2] or bored[3] == bored[4] == bored[5] or bored[6] == bored[7] == bored[8] or bored[0] == bored[4] == bored[8] or bored[2] == bored[4] == bored[6] or bored[0] == bored[3] == bored[6] or bored[1] == bored[4] == bored[7] or bored[2] == bored[5] == bored[8]:
      print(Turn, "wins")
      play = False
    else:
      if turn == False:
        x -= 1
        print(turn, "plese enter a vaild space")
        turn = True
      elif Turn == "x ":
        Turn = "o "
      elif Turn == "o ":
        Turn = "x "
  reset()
reset()