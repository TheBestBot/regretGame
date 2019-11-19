print("Welcome to Regret,\n\na happy little innocent text based semi-procedurally generated wizardry dungeon crawler RPG.\n")
fails = 0
import sys, time

def Piece(text, speed):
  for c in text:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.05)
  print


while True:
  Piece("How much do you regret? Low or enough?\n")
  difficulty = input().strip().lower()
  print()
  if len(difficulty) != 0:
    if difficulty[0][0] == "l":
      time.sleep(0.5)
      print("Low? It's a simple start.\n\n")
      break
    elif difficulty[0][0] == "e":
      time.sleep(0.5)
      print("Enough? That's going to hurt, however much that is.\n\n")
      break
    else:
      time.sleep(0.5)
      print("Thats not what I asked for.")
      fails += 1
  else:
    time.sleep(0.5)
    print("Thats not what I asked for.")
    fails += 1
