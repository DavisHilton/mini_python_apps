start = "Car started ... Ready to go!!"
stop = "Car stopped"  
started = False
stopped = False

help = '''
start - to start the car
stop - to stop the car
quit - to exit
''' 
instruction = ""
while instruction != quit: 
    instruction = input(">").lower()  
    if instruction == 'help':
        print(help)
    elif instruction == 'stop':
        if stopped:
            print("Car is already stopped") 
        else:
            stopped =True
            print(stopped)
    elif instruction == 'start':
        if started:
            print("Car is already started") 
        else:
            started = True
            print(start)   
    elif instruction == 'quit':
        break
    else:
        print("Sorry I don't undestand.")

