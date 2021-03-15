#!/usr/local/file/bin/python3
# An Number Guesser for project making experience bulding.
'''
__author__='rohith sasi'
__scriptname__='G.A ame ( A number guessing game  ) '

'''

    
    ########################################
    #   Name of author : Rohith Sasi        #
    #   subject:  A number guesser .(vb1)   #
    #for more details: 123rohith4@gmail.com #
    #   origin: India                       #
    #   get me through insta : rohith_9991  #
    #########################################



# importing 2 needed modules for later use

try:
    import random
    import sys
    import os
    import time
except ImportError:     # exceptions for import errors.
    print('sorry some error happened while importing modules..(check once again )')
    print(' sometimes some  dependencies may not be  installed: (write)\n1) pip install os\n2) pip install time')
    exit()

# Using system commands for certain uses.
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')
sr='''\033[0;31m A number guesser game by: 
        

        ___     _    _ _   _
       | _ \___| |_ (_) |_| |_
       |   / _ \ ' \| |  _| ' \ 
       |_|_\___/_||_|_|\__|_||_|
                                  '''

print(sr)
time.sleep(2)


# Using system commands for certain uses.
if os.name=='nt':
    os.system('cls')
else:   
    os.system('clear')


w='\033[1;0m'

# logo for the guesser game.

logo='''
      _|_|_|        _|_|
    _|            _|    _|      _|_|_|  _|_|      _|_|
    _|  _|_|      _|_|_|_|      _|    _|    _|  _|_|_|_|
    _|    _|      _|    _|      _|    _|    _|  _|
      _|_|_|  _|  _|    _|      _|    _|    _|    _|_|_|
'''

# bulding random choices
ch=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m'])
print(ch,logo,w)

# selections for figuring out number for the players
if ch =='\033[1;31m':
    print('\033[1;34m','A number guesser  game for begginners')
    print()
    print('os :', sys.platform)
    
    print('NOTE: The number will be always == or < 10')
else:
    print('\033[1;31m','A number guesser  game for begginners')
    
    print()
    print('os :', sys.platform )
        
    print('NOTE: The number will be always == or < 10')

print(w)
print()
choice_num=random.randrange(1,10)


for i in range(1,7):
    print('\033[1;31m','your chance no:',i)
    print('-'*30)
    print()
    try:        # exception handling for input errors
        
        num=int(input('number:\033[1;36m'))
        print(w)
        
    except ValueError:
        print('The value given is not a number,an error occured.(make sure you typed a number ....) ',w)
        exit()
    
    except KeyboardInterrupt:
        print('The keyboard intereption occured(pls make sure to not type anything other than numbers....) ',w)
        exit() 
    except EOFError:                                                     
        print('\nthe tester.py had been stopped working due to an typing error.',w)
        exit()    
                                                                
   
    if num==choice_num:
        print('\033[1;31m','congragulations , you have won the game.',w)
        exit()
    elif num > choice_num:
        print('\033[3;34m','ok,good... but the number is lower than',str(num),'\nThink some lower digits...',w)
    elif num < choice_num:
        print('\033[3;34m','ok,good... but the number is higher than,',str(num),'\nThinksome higher digits...',w)
    
    else:
        print('\033[1;31','something else happened , pls try again .... ',w)
    
        exit()
    if i ==  6:
        print('\t\033[0;31m -chances all have been finished-',w)
        exit()
    

