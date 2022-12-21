import random
WORDS = ['PLANE','SHIP','TRUCK','HELICOPTER', 'BALLOON', 'CYCLE']
display = []
rounds = 10

def main():
  words = random.choice(WORDS)
  print(words)

  for i in words :
    display.append('_')
  print(display)

  for i in range(rounds):
    print("Round", i + 1)
    guess = input("Enter your guess [A-Z]:")
    guess = guess.upper()  

    for j in range(len(words)):
      if words[j] == guess.upper():
        display[j] = words[j]
    print (display)  

    count = 0
    for k in display:
      if k != '_':
        count += 1
        
    if count == len(words):
      print ("Congratulation!, the word is:", words)
      break
  print ("Thank You")    
    
main()

            
                
