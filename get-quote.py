import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  quotes.append("Make hay while sunshine")
  f.close()

  last= len(quotes)-1
  rnd= random.randint(0, last)
  arnd= random.randint(0, last)

  print(f'{quotes[rnd]}{quotes[arnd]}')
  #print(quotes[arnd])

if __name__== "__main__":
  primary()
