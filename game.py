#Time is a library which will allow me to use time.sleep() later on in the code
import time

#name variable is to ask for the user's name and to have later on
name = input('What is your Name: ')

#Greetings
print('Greetings',name)

#Laying out Instructions for the game that is to come
print('All your answers should be in (yes/no) format MUST BE LOWERCASE')
print('There will be a series of questions, AnWsEr CaReFuLlY!')

#this function is near the end of the game but in order to call it has to be stated beforehand
#second_start will have to do mostly with the second portion of the game, after you survived
def second_start():
    #time.sleep() allows me to have a delay from the moment it executes until it actually gives me an output
    time.sleep(1)
    print(name, 'I must congratulate you for coming this far')
    #ask_game is an input that will ask the user if they enjoyed playing the first portion of the game
    ask_game = input('Did you have fun in the first game? ')
    #if ask_game == 'yes' if the users answer is yes they will be awarded a badge for completing the game the "correct" way
    if ask_game == 'yes':
        print('You know how to please the maker')
        time.sleep(1)
        print('What if I told you there is no second game')
        time.sleep(0.5)
        print('Your ability to make it this far is rather surprising')
        time.sleep(1)
        print('YOU HAVE BEEN AWARDED A BADGE FOR COMPLETING THE GAME "CORRECTLY"')
        time.sleep(0.5)
        print('🏅🏅🏅')
    #elif ask_game == 'no' if the users answer is no it will lead the user to a question after
    elif ask_game == 'no':
        print('BLASPHEMY')
        time.sleep(1)
        #the regret input builds upon the previous question about if they liked the first game, after they answered no it asks ->
        # -> the user if they regret their decision
        regret = input('Do YoU ReGrEt YoUr DeCiSiOn??? ')
        #if players answer to the regret input is yes, they will be forgiven but pay the price for their mistakes
        if regret == 'yes':
            print('You have been forgiven')
            time.sleep(0.5)
            print('Sadly your end has come')
            time.sleep(0.1)
            print('...')
            time.sleep(0.1)
            print('...')
            time.sleep(0.1)
            print('...')
            time.sleep(0.1)
            print('...')
            time.sleep(0.1)
            print('...')
            time.sleep(0.1)
            print('...')
            time.sleep(0.1)
            print('Unexplained Death has Occured*')
        #if the player had answered no to the regret input it will cause them to die
        elif regret == 'no':
            print('SOME EXTERNAL POWER HAS TAKEN YOUR LIFE*')
        #whenever this UNSKILLED statement appears it basically means that the user has written something other than yes or no
        #note: the comment on line above is not True for the question asking how is your day?
        else:
            print('UNSKILLED (DIED FOR NOT FOLLOWING ORDERS*)')
    else:
        print('UNSKILLED (DIED FOR NOT FOLLOWING ORDERS*)')

#After answering the first question(How is your day?), if your answer is NOT yes or no you will be taken here
def hard():
    print('Due to your mistakes we may have to do this the hard way')
    time.sleep(1)
    #ask_teach is simply asking if Mr.Nagra is the best Comp Sci Teacher
    ask_teach = input('Is Mr.Nagra the best Comp Sci Teacher? ')
    #if the user answered yes to ask_teach question it will proceed immediately to the second_start function
    if ask_teach == 'yes':
        print("Let's Agree to Disagree")
        time.sleep(1)
        print('On to the second game')
        time.sleep(0.5)
        #second_start() is meant for calling a function, it will always be written in function_name() format
        second_start()
    #if ask_teach was answered as no, not only will Mr.Nagra be informed but you would also die
    elif ask_teach == 'no':
        print('Mr.Nagra will be informed of this')
        time.sleep(1)
        print('You have Died for Incompetence*')
    else:
        print('UNSKILLED (DIED FOR NOT FOLLOWING ORDERS*)')

#the easy function ties back to the first question(how is your day?), if the player had answered yes or no they will be taken here
def easy():
    print('You are now in the easy mode')
    #the ask_2 input asks the user if they happen to be thirsy at the moment
    ask2 = input('are you thirsty? ')
    #if the user answered yes to the ask_2 question it will ask them to get water
    if ask2 == "yes":
        print('Go get a glass of water')
        time.sleep(2)
        #ask3 is meant to pressure the player in getting water, we cant have the payer dying of thirst
        ask3 = input('Did you get water? ')
        #if the player answer yes to ask3 then it will redirect the player to the second game
        if ask3 == 'yes':
            print('Good Job')
            time.sleep(0.5)
            print('Now for the second game')
            #this line calls the second_start function
            second_start()
        #if the player answered no to ask3 it will 💀💀💀
        elif ask3 == 'no':
            #these skulls will appear on the screen
            print('💀💀💀')
            time.sleep(1)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(0.0001)
            print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
            time.sleep(2)
            #after diplaying skulls another question will be thrown at the player
            #the ask_water input is meant to give the player one last chance to get water
            ask_water = input('Last chance, WILL you get WATER? ')
            #if your answer to ask_water is yes it will cause there to be "20 second" countdown
            #using time.sleep() we are able to space the time the numbers are outputted at(note: meant to be 0.5 instead of 1)
            if ask_water == 'yes':
                print('YOU HAVE 20 SeCoNdS...')
                time.sleep(5)
                print('COUNTDOWN WILL BEGIN NOW')
                time.sleep(2)
                print(20)
                time.sleep(0.5)
                print(19)
                time.sleep(0.5)
                print(18)
                time.sleep(0.5)
                print(17)
                time.sleep(0.5)
                print(16)
                time.sleep(0.5)
                print(15)
                time.sleep(0.5)
                print(14)
                time.sleep(0.5)
                print(13)
                time.sleep(0.5)
                print(12)
                time.sleep(0.5)
                print(11)
                time.sleep(0.5)
                print(10)
                time.sleep(0.5)
                print(9)
                time.sleep(0.5)
                print(8)
                time.sleep(0.5)
                print(7)
                time.sleep(0.5)
                print(6)
                time.sleep(0.5)
                print(5)
                time.sleep(0.5)
                print(4)
                time.sleep(0.5)
                print(3)
                time.sleep(0.5)
                print(2)
                time.sleep(0.5)
                print(1)
                time.sleep(1)
                #the ask_last input is meant to ask the player if they got the water in the given time or not
                ask_last = input('Did you get the water? ')
                #if the answer to ask_last was yes it will ask the player if they want to keep playing
                if ask_last == 'yes':
                    print('My Job is done, your thirst has been quenched')
                    #ask_q input is to ask the player if they would like to keep playing or not
                    ask_q = input('Would you like to keep playing? ')
                    #if ask_q was answered as yes it will redirect the user to the second_start function
                    if ask_q == 'yes':
                        print('Let us start again')
                        second_start()
                    #if the answer to ask_q was no it will leave a small farewell(ONE OF 2 GOOD ENDINGS)
                    elif ask_q == 'no':
                        print('Goodbye')
                    else:
                        print('UNSKILLED (DIED FOR NOT FOLLOWING ORDERS*)')
                #if ask_last was answered as no the player will die of thirst
                elif ask_last == 'no':
                    print('DIES OF THIRST*')
                else:
                    print('UNSKILLED (DIED FOR NOT FOLLOWING ORDERS*)')
            #if the player answered no to the ask_water input their journey will end due to thirst
            elif ask_water == 'no':
                print('DIES OF THIRST*')
            else:
                print('UNSKILLED (DIED FOR NOT FOLLOWING ORDERS*)')
        else:
            print('UNSKILLED (DIED FOR NOT FOLLOWING ORDERS*)')
    #if ask2 is answered as no it will cause for the user to drop dead
    elif ask2 == 'no':
        print('DIES OF THIRST*')
    else:
        print('UNSKILLED (DIED FOR NOT FOLLOWING ORDERS*)')

#arguably the most important function in this long journey, the START of the game
#this start() function is what allows the player to enjoy this fascinating experience made by Emmanuel Lopez-Vanegas
#after the user inputs their name it will run the start() function
def start():
    #the ask1 input will ask the player about their day, dependent on their answer they might get System32 Deleted(it does not)
    ask1 = input('How is your day? ')
    #if ask1 was either answered as yes or no it will lead the player to the easy mode of the game(easy= more fun and longer)
    if ask1 == "yes" or ask1 == "no":
        print("Your answer doesnt make sense but let's proceed")
        #redirected to the easy function
        easy()
    #if any other answer is submitted it will cause for the player to take the hard mode
    #(hard = absurdly difficult and short)
    else:
        print("I said answer YES OR NO")
        time.sleep(2)
        #redirected to the hard function
        hard()
start()