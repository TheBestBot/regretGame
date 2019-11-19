print("Welcome to Regret,\n\na happy little innocent text based semi-procedurally generated wizardry dungeon crawler RPG.\n")
while True:
  difficulty = input("How much do you regret? Low or high?\n").strip().lower()
  print("")
  if difficulty[0][0] == "l":
    print("Low. It's a simple start.\n\n")
  elif difficulty[0][0] == "h":
    print('sus box')
  else:
    print("thats not what I asked for")
  #if letter == :
  #  print("There is a P!")
  # break #If a p is found, exit the loop

#else: #Otherwise if no P, tell user
#  print("There is no letter P in the phrase")