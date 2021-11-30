print("Welcome to treasure island where either DEATH or GLORY await, before you will test your mantle can you surive the challenges that so many before you failed? Or will you stand above the rest?")

greenDoor = ("You've walked ito a bright green door! You take two steps in the darkness and see a treasure chest. You quickly approch, bend over open the chest. Only to be greeted with 500 teeth. You are instantly devoured and the box closes \n GAME OVER")

blueDoor = ("You open the door and a spear plunged through your chest. Falling to your knees you fall over and burst into flames. \n GAME OVER")

yellowDoor = ("Congrats you are a 200 billion gold coins have been deposited into your crypto accountt! Go and change the world")

choiceONe = input("You walk along the beach, ahead of you there is a fork in your path you can go either left or right: ").lower()
if choiceONe == "left":
    print("You walk 2 miles and approach a pier looking off into the distance you see a small island.")
    choiceTwo = input("You can swim to the island or you can wait: ").lower()
    if choiceTwo == "wait":
        print("A bridge magically appears from under water so you walk across to the island.")
        choiceThree = input('On the island now..... a giant ant jumps off a mountain, headed straight towards you. You fall on the ground in fear and get swalled in the ants tummy you you are teleported to the temple. As you stand up you are now facing three doors Blue, Yellow, Green. which will you choose?:  ').lower()    
        if choiceThree == "blue":
            print(blueDoor)
        elif choiceThree == "green":
            print(greenDoor)
        elif choiceThree == "yellow":        
            print("yellowDoor")
            
    else:
        print('A shark bites off your knee caps')
else:
  print('A meteor falls and crushes you')    


