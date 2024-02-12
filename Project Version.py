import pyttsx3
import random
import csv
from datetime import date


'''                 This is a number guessing game                          '''


#----------------------- PART-I : Function definition part --------------------

#1 function to read out the argument passed to it.
engine = pyttsx3.init()
def speak(text,*var,ends = ' '):
    #engine.setProperty('rate',200)
    engine.say(text)
    # checking if any arg has been passed to tuple var
    if len(var) == 0:
        print(text)
    else:

        print(text, end = ' ')
        for word in var:
            engine.say(word)
            #checking if the last element of var has been reached
            #if it has then end should not be a newline character
            if word == var[-1]:
                print(word, end = ends)
            else:
                print(word, end = ' ')   
    
    engine.runAndWait()

    
# This list stores the nos which stands for different hints
key_list = [1,2,3,4,5,6,7,8]
#2 Function to provide the hint keys in based on which hint will be given 
def hintkey():        
    # Taking a random hint no from the list & storing in variable no
    no = random.choice(key_list)
    key_list.remove(no)
    return no

#3 Function to provide hint acc. to the hintkey passed in its argument
def get_hint(ii):
    if ran < 0:
        length = len(str(ran)) - 1
    else:
        length = len(str(ran))
    if ii == 1:
        div_list = [3,4,5,6,7,8,9]
        div = random.choice(div_list) 
        while True:
            if ran % div != 0:
                speak("Subtracting",ran % div,"from the number will make it divisible by",div,"") 
                break
            else:
                div_list.remove(div)
                div = random.choice(div_list)
    
    elif ii == 2:
       if ran < 0:
           copyran = ran*(-1)
       else:
           copyran = ran
       i = 2
       prime = True
       while i <= copyran//2:   
           if copyran % i == 0:
               prime = False
               break
           i += 1
       if prime == False:
           if u_limit - l_limit < 100:
               speak('It is a composite number')
           else:
               ii = hintkey()
               get_hint(ii)
       else:
           speak("It is a prime number")
               
        
    elif ii == 3:
       if 2 in key_list:
            if u_limit - l_limit > 100:
                if ran % 2 == 0:
                    speak("The number is even.")
                else:
                    speak("The number is odd.")
       else:
           ii = hintkey()
           get_hint(ii)  
   
    elif ii == 4:
       div2_list = [11,12,13,14,15,16,17,18,19]
       div2 = random.choice(div2_list)
       while True:
           if ran % div2 != 0:      
               add_num = div2 - (ran % div2) 
               speak("Adding",add_num,"to the number will make it divisible by",div2)
               break
           else:
               div2_list.remove(div2)
               div2 = random.choice(div2_list)
           
    elif ii == 5:
        if length == 1:
            speak('Its a single digit number')
        elif length == 2:
            speak('Its a double digit number')
        else:
            index = random.randint(0,length-1)
            if index == 1:
                place = '1st'
            elif index == 2:
                place = '2nd'
            elif index == 3:
                place == '3rd'
            else:
                place = str(index) + 'th'
            speak('It has',str(ran)[index],'in its',place,'index.')
    
    elif ii == 6:
         if ran < 0:
             copyran = ran*(-1)
         else:
             copyran = ran
         tmp = copyran
         rev = 0
         while tmp != 0:
             cur = tmp % 10
             rev = rev * 10 + cur
             tmp = tmp//10
         if copyran == rev:
             speak('It is a Palindrome')
         else:
             ii = hintkey()
             get_hint(ii)
    
    elif ii == 7:
        if len(str(ran)) > 2:
            speak("It is a",length,"digit number")
        else:
            ii = hintkey()
            get_hint(ii)
    
    elif ii == 8:
        if l_limit < 0:
            if ran < 0:
                speak("It is a negative number")
            else:
                speak("It is a positive number")
        else:
            ii = hintkey()
            get_hint(ii)
   
# ---------------------- End of function definitions --------------------------

# About & Options part
print('\n')
print('='*100,'\n\n')
speak('Welcome,\n')
speak('This is a number guessing game')
#speak('And I am Artemis, and I will be your interface all through the game')
speak("\nRead 'ABOUT' & 'OPTIONS' before proceeding? Y/N : ")
q1 = input().upper()

if  q1 in ('YES','Y'):
    # Opening the Game_About file where about the game is stored
    about_file = open(".//Game_About.txt")
    s = about_file.read()
    about_file.close()
    print(s)
#------------------------------------------------------------------------------

                        # PART-2 : Options setting part

# This loop will help the user to play another round of game directly after
# finishing one without having to start all over again.
while True:
    # Asking name of the pkayer
    speak('\nEnter name: ', ends = '')
    p_name = input().title()
    
    speak('\nChoose game mode:-')
    print("AUTO/MANUAL (A/M) : ",end = '')
    g_mode = input().upper()
    
    # Setting all parameters for Manual mode
    while True:
        if g_mode in ('M','MANUAL'):
            g_mode = 'MAN'
            diff = '-'
            speak("Enter guessing range :-")
            speak("Lower limit : ",ends = '')
            l_limit = int(input())
            speak("Upper limit : ",ends = '')
            u_limit = int(input()) 
            
            g_range = u_limit - l_limit 
            if g_range <= 50:
                max_attempt = 10
                max_hints = 3      
            elif g_range <= 100:
                max_attempt = 15
                max_hints = 4      
            elif g_range <= 300:
                max_attempt = 20
                max_hints = 5     
            elif g_range <= 500:
                max_attempt = 25
                max_hints = 5      
            else :
                max_attempt = 30
                max_hints = 5
            
            speak("Enter number of attempts you want (not more than",max_attempt,"):",ends = '')
            n_att = int(input())
            speak("Enter number of hints you want (not more than",max_hints,"):", ends = '')
            n_hints = int(input())
           # The loop part below checks if the entered values are not greater
           # the max values allowed
            while True:
                if n_att == 0:
                    speak("INVALID INPUT! (No. of attempts can't be zero)")
                    speak("Enter number of attempts: ", ends = '')
                    n_att = int(input())   
                elif n_att > max_attempt:
                    speak("Number of attempts should not be more than ",max_attempt,"!") 
                    speak("Enter valid number of attempts : ",ends = '')
                    n_att = int(input()) 
                if n_hints > max_hints:
                    speak("Number of hints should not exceed",max_hints,"!")
                    speak("Enter valid number of hints: ",ends = '')
                    n_hints = int(input())        
                else:
                    break
            break
        
        # sellting all parameters of AUTO mode
        elif g_mode in ('A','AUTO'):
            g_mode = 'AUT'
            speak("\nEnter difficulty level:-")
            print("Easy/Medium/Hard/Advanced/Wizard: ",end = '')
            diff = input().upper()
            while True:
                if diff in ('E','EASY'):
                    diff = 'EAS'
                    l_limit = 0
                    u_limit = 50
                    n_att = 4
                    n_hints = 2
                    break
                elif diff in ('M','MEDIUM'):
                    diff = 'MED'
                    l_limit = 0
                    u_limit = 100
                    n_att = 6
                    n_hints = 3
                    break
                elif diff in ('H','HARD'):
                    diff = 'HAR'
                    l_limit = -100
                    u_limit = 100
                    n_att = 8
                    n_hints = 4
                    break
                elif diff in ('A','ADVANCED'):
                    diff = 'ADV'
                    l_limit = -300
                    u_limit = 300
                    n_att = 10
                    n_hints = 5
                    break       
                elif diff in ('W','WIZARD'):
                    diff = 'WIZ'
                    l_limit = -500
                    u_limit = 500
                    n_att = 15
                    n_hints = 5
                    break
                else:
                    speak("Enter a valid difficulty level (E/M/H/A/W): ",ends = '')
                    diff = input().upper()
            break
                
        else:
            speak("Invalid input!")
            speak("Enter a valid game mode A/M:", ends = '') 
            g_mode = input().upper() 
        
    # setting the initial points that the player has
    pts = n_att*5 + n_hints*10
    
    # displaying a summary of options that the user has selected
    print('\n')
    speak("         SUMMARY ")
    print('='*25)
    print("  Name          :  ",p_name)
    print("  Game Mode     :  ",g_mode)
    if g_mode == 'AUT':
        print("  Difficulty    :  ",diff)
    print("  Lower Limit   :  ",l_limit)
    print("  Upper limit   :  ",u_limit)
    print("  Attempts      :  ",n_att)
    print("  Hints         :  ",n_hints)
    print('='*25)             
    
    
    speak("\nPress Enter to continue: ",ends = '')
    ask2 = input()
    
#------------------------- End of Part 2 --------------------------------------
    # PART-3: Generation of random no & guessing part
    
    
    #generating the random number & storing in variable 'ran'
    ran = random.randint(l_limit,u_limit)   
    if l_limit < 0:
        note = 'NOTE : Hints are equally applicable to both negative & positive numbers.'
        speak(note)

    # variable to take count of the no. of attempts
    i = 1             
    # variable to take count of the hints used
    h_used = 0
    guess = False
    
    # actual playing round begins
    while i <= n_att:
       print('\nPoints:', pts)
       
       if n_att == i:
           speak("Last attempt!: ",ends = '')
       else:
           speak('Attempt',i, ends = '.')
       
       # if no hint is remaining then the player is directly asked to enter guess
       if n_hints == 0:
           while True:
               speak("\nEnter guess: ",ends='')
               user_guess = input()
               if type(user_guess) == str():
                   if user_guess in ('h','hints'):
                       speak("All hints exhausted!",ends = '\n')
                   else:
                       speak('Invalid Input',ends = '')
               else:
                   user_guess = int(user_guess)
                   break
       # else if hint is available, the player is being asked either to enter guess 
       # or to take hint
       elif n_hints > 0:
           print("\nHints Remaining: ",n_hints)
           speak("Enter guess or (H for hint): ", ends = '')
           user_guess = input()
           
           if user_guess.isdigit():
               user_guess = int(user_guess)
           
           elif user_guess in ('h','H'):
               # calling function to get hint numbers & storing in varable 'ii'
               ii = hintkey()
               
               speak('-- HINT --  : ',ends = '')
               # calling function to get hint
               get_hint(ii)
               # deducting points for taking hint
               pts -= 10
               # increasing hints used by 1
               h_used += 1
               # asking to make the guess after taking hint
               speak("\nNow enter guess: ",ends = '')
               user_guess = int(input())
            
               # decreasing hints by 1 after every hint taken
               n_hints -= 1
       
       if user_guess == ran:
            guess = True
            break
    
       # increasing the attemps taken
       i += 1
       # deducting points for each attempt taken
       pts -= 5
    #------------------------- End of Guess Loop ------------------------------
    
    if guess == True:    
       speak("\nYou have guessed the number")
       speak("YOU WIN!")
       status = 'WON'
    else:   
       speak("\nGAME OVER!")      
       speak("The number was",ran)
       status = 'LOST'
       pts = 0
        
    speak('\npoints:',pts)    
    
    # ---File Storage part---
    date = date.today()
    g_range = u_limit - l_limit
    # Format of player info/ coloumn headings: 
    # [name,game mode,difficulty,guess range,hints,attempts,W/L,points,the Random no,date]
    
    # Opening the file used to store player info
    p_file = open('.//Player_stats.csv','a')
    p_writer = csv.writer(p_file)
    info_list = [p_name,g_mode,diff,g_range,h_used,i,status,pts,ran,date]
    # storing the player info for one round of game into the Player_stats file
    p_writer.writerow(info_list)
    p_file.close()

    # asking user whether to have another round of game
    speak('\nAnother round? Y/N :',ends = '')
    ask3 = input().lower()
    if ask3 in ('y','yes'):
        continue
    else:
        speak('Exiting...')
        print("\n",'='*100,"\n\n")
        break
#---------------------------- PART 3 END --------------------------------------        
#                              CODE END
