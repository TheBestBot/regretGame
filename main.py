import sys, time, random 

fails = 0
difficulty = 0

health = 100
attack = 10
block = 0

def piece(text = """Lorem Ipsum,
Neque porro quisquam est qui dolorem ipsum quia dolor sit amet,
consectetur, adipisci velit...\n\n""", delay = 0.2, speed = 0.03):
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(speed)
  print
  time.sleep(delay)


#intro scene

piece("Welcome to Regret.\n\n", 0.5, 0.15)

piece("Regret, a happy little innocent text based semi-procedurally generated wizardry dungeon crawler RPG.\n\n", 0.5)

while True:
  piece("How much do you regret? Low or enough?\n")
  difficultyC = input().strip().lower()
  time.sleep(0.5)
  print("")

  if len(difficultyC) != 0:
    if difficultyC[0][0] == "l":
      piece("Low? It's a simple start.\n\n")
      difficulty = 0
      break
    elif difficultyC[0][0] == "e":
      piece("Enough? That's going to hurt, however much that is.\n\n")
      difficulty = 1
      break
    else:
      piece("Thats not what I asked for.\n")
      fails += 1
  else:
    piece("Thats not what I asked for.\n")
    fails += 1


def encounter(level = 0, diff = difficulty):
  global fails
  global health
  global block
  global attack
  level += diff
  if random.choice([0]) == 0:
    #high hp hostile
    piece("A wild goblin appears!\n")
    hp = round(100+3*level)
    attk = round(5+0.4*level)
    blk = round(5+0.4*level)

    #0 is attack 1 is block
    while True:
      if random.choice([0, 1]) == 0:
        piece("The goblin intends to attack for {} damge.\n".format(attk))
        action = 0
      else:
        piece("The goblin intends to block {} points.\n".format(blk))
        action = 1
      
      while True:
        piece("Attack or Block?")
        option = input().strip().lower()
        time.sleep(0.5)
        print("")

        if len(option) != 0:
          if option[0][0] == "a":
            piece("You attack the goblin for {} damage!\n".format(attack))

          if blk == 0:
            hp -= attack
 

          elif option[0][0] == "b":
            piece("Enough? That's going to hurt, however much that is.\n\n")
            option = 1
            break
          else:
            piece("Thats not what I asked for.\n")
            fails += 1
        else:
          piece("Thats not what I asked for.\n")
          fails += 1

  else:
    #random bandit
    piece("A hostile bandit appears!")
    hp = round(50+1*level)
    attk = round(10+1*level)
    blk = round(5+1*level)

    #0 is attack 1 is block
    if random.choice([0, 1]) == 0:
      piece("The bandit intends to attack for {} damge.\n".format(attk))
      action = 0
    else:
      piece("The bandit intends to block {} points.\n".format(blk))
      action = 1

encounter(10)

if difficulty ==0:
  piece("""It's a day in the forest.
There isn't much here but your small camp.
Then you rember, what has happened, it hits you like a truck.
The day is young but time is the most valualbe resource here.
There is no escaping what is comming.
Only a few days remain until the last bridge will be blocked.\n\n""")
  piece("""You'r still hurt from the prevous day, you could rest here for the day or travel on.
What are you doing?""")
  choice = input().strip().lower()
  

