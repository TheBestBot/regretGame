print("Welcome to Regret,\n\na happy little innocent text based semi-procedurally generated wizardry dungeon crawler RPG.\n")
fails = 0

while True:
  difficulty = input("How much do you regret? Low or enough?\n").strip().lower()
  print()
  if len(difficulty) != 0:
    if difficulty[0][0] == "l":
      print("Low? It's a simple start.\n\n")
    elif difficulty[0][0] == "e":
      print("Enough? That's going to hurt, however much that is.\n\n")
    else:
      print("Thats not what I asked for.")
      fails += 1
  else:
    print("Thats not what I asked for.")
    fails += 1
  #if letter == :
  #  print("There is a P!")
  # break #If a p is found, exit the loop

#else: #Otherwise if no P, tell user
#  print("There is no letter P in the phrase")