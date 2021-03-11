command = ""
print("Welcome to the totally not questionable game! Wooo.....")
print("Type help for options!")
print("Side note: Put all responses in lower case letters or else it wont work!")
while command != "quit":
  command = input("> ").lower()
  if command == "start":
    print(" ")
    print("Your virtual, non GUI car has started... Cool, I guess. :/ Hey at least it's not broken anymore. Now you can resume your journey of  getting milk from the supermarket! ¯\_(ツ)_/¯")
    print(" ")
    print('Oh shit, your car just broke down again. This car was a massive scam. Type "stop" to make sure no more damage is done')
  elif command == "stop":
    print(" ")
    print("You've stopped your useless car. Should you burn it? Yes or No")
  elif command == "yes":
    print(" ")
    print("""You've set fire to your useless, horrible car. You get a feeling of..... Happiness.
  Watching the car that broke down on you just a few minutes ago.""")
    print(" ")
    print("""But now there's a problem. it's getting late and you were suppose to get
    home before dinner with the milk that you promised you'd get. But luckily you have a bit of spare money to
    give to an Ulift. So you go to the Ulift app and do all of the boring stuff to get a Ulift driver. They came
    in about 5 minutes to drive you to your house. Nice! But your parents are gonna be mad as fuck that you 
    burned the car. Type "home" to enter your home.
    """)
  elif command == "no":
    print(" ")
    print("""You didn't burn your car. But you notice that its getting late and that you were suppose to get
    home before dinner with the milk that you promised you'd get. But luckily you have a bit of spare money to
    give to an Ulift. So you go to the Ulift app and do all of the boring stuff to get a Ulift driver. They came
    in about 5 minutes to drive you to your house. Nice! But your parents are gonna be mad as fuck that the car
    broke down. Type "home" to enter your home""")
  elif command == "home":
    print(" ")
    print("""You enter your house to find.. nobody. You checked every single corner of the house to find your parents, but
    they're nowhere. But you find a message left behind. Type "observe" to observe the message """)
  elif command == "observe":
    print(" ")
    print("""You observe the drawing. Drawn in blood: See no evil, Hear no evil, Speak no evil. It sends chills down your spine.
    the blood probably belongs to your parents. Before your able to think of who would of done this. Someone jumps you. You get stabbed multiple times. And then..... blackness.
    """)
    print(" ")

    print("TO BE CONTINUED")
    print("""Type "quit" to quit out of the game """)
  elif command == "help":
    print("""
    start - to start the game
   help - to bring up this dialog
    quit - to quit out of this game ;-;
    """)
  elif command == "quit":
    break  
  else:
    print("Sorry, I don't understand that command")