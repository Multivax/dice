import random
running = 1
dice = int
rollNr = int
while running == 1:  # start main loop
    command = input("What do you want to do? ").split()  # get user input and place in list
    try:  # prevent program from crashing when user leaves input blank
        if command[0] == "roll":  # command to roll,
            if len(command) <= 1:
                print("Please put the numbers of the dice you want to roll behind the command")
            else:
                for i, x in enumerate(command):  # this loop turns all numbers from strings to ints
                    try:
                        command[i] = int(x)
                    except ValueError:
                        pass
                for rollNr in range(len(command)):  # loop to roll all the dice
                    if rollNr == 0:  # print that rolling and workaround for start at 0
                        print("You rolled:")
                    else:  # roll the dice
                        if type(command[rollNr]) != int or (command[rollNr] <= 1): # error if element is not a number
                            print("Roll {}: Invalid dice".format(rollNr))
                        else:  # roll the dice
                            print("Roll {}: {} out of {}".format(rollNr, random.randrange(1, command[rollNr] + 1), command[rollNr]))
                    rollNr += 1  # increment the loop
        elif command[0] == "exit":  # command to exit the loop
            running = 0
        else:  # for invalid commands
            print("Invalid Command")
    except IndexError:
        print("Invalid Command")
