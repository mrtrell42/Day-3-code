year = int(input("what year is it? "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print('Leap year')
        else:
            print('not leap')    
    else:
        print('Leap')        
else:
    print('Not leap')            