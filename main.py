# imports
import random

# constants
STARTING_CREDIT = 1
PLAY_COST = -0.2
WINNINGS = {
  1: 0.5, # two of the same
  2: 1, # three of the same
  3: 5, # three bells
  4: -1, # two skulls
  5: -(10**1000) # three skulls
}
OPTIONS = ['cherry', 'bell', 'lemon', 'orange', 'star', 'skulls']
ROLLS = 3

# variables
balance = STARTING_CREDIT

# functions
def handleResults(results):
  global balance
  msg = ''
  for i in range(ROLLS):
    msg += OPTIONS[results[i]] + ' '
  print(msg)

  for i in range(6):
    count = results.count(i-1)
    if i == 5:
      if count == 2:
        balance += WINNINGS[4]
      elif count == 3:
        balance += WINNINGS[5]
    if i == 1 and count == 3:
      balance += WINNINGS[3]
    elif count == 3:
      balance += WINNINGS[2]
    elif count == 2:
      balance += WINNINGS[1]
  if balance <= 0:
    print('you lost all your money! Resetting...')
    balance = STARTING_CREDIT

def generateResults():
  global balance
  balance += PLAY_COST
  balance = round(balance, 2)
  res = []
  for _ in range(ROLLS):
    res.append(random.randint(0, 5))
  handleResults(res)


# command cases
def CaseHelp():
  return print("""
## HELP ##

Good luck, you're on your own. This hasn't been added yet.
  """)

def CaseQuit():
  return exit()

def CasePlay():
  return generateResults()

case = {
  "help": CaseHelp,
  "quit": CaseQuit,
  "exit": CaseQuit,
  "play": CasePlay,
}

# main
if __name__ == "__main__":
  while True:
    print(f'Current balance: £{balance}')
    inp = input('> ').lower()
    try:
      case[inp]()
    except Exception as err:
      if inp == 'quit' or inp == 'exit':
        break
      if inp in case:
        print(f'Something went wrong. \n{err}')
      else:
        print('Unknown command. Type "help" for a list of commands.')
      continue
