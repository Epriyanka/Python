from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
import os
# use Colorama to make Termcolor work on Windows too
init()
# then use Termcolor for all colored text output
os.system('cls')
print(Fore.RED+Back.GREEN + "{:^80}".format("Enter Student Mark"),end='')
print(Back.RESET+'',end='')
print("Enter Student Name       : ")
print("Enter Registration Number: ")
print("Enter Tamil Mark         : ")
print("Enter English Mark       : ")
print("Enter Maths Mark         : ")
print("Enter Science Mark       : ")
print("Enter Social Science Mark: ")


print("\033[2;30H",end="")
name=input()
print("\033[3;30H",end="")
reg=input()
print("\033[4;30H",end="")
t=input()
print("\033[5;30H",end="")
e=input()
print("\033[6;30H",end="")
m=input()
print("\033[7;30H",end="")
s=input()
print("\033[8;30H",end="")
ss=input()
tot=int(t)+int(e)+int(m)+int(s)+int(ss)
avg=tot/5
print(Fore.YELLOW)
print("\nStudent Name       : ",name)
print("Registration Number: ",reg)
print("Tamil Mark         : ",t)
print("English Mark       : ",e)
print("Maths Mark         : ",m)
print("Science Mark       : ",s)
print("Social Science Mark: ",ss)
#print(Fore.BLUE+'',end='')
print("\033[35m\033[47m",end='')
print("Total              : ",tot)
print("Average            : ",avg)


"""ESC [ 0 m       # reset all (colors and brightness)
ESC [ 1 m       # bright
ESC [ 2 m       # dim (looks same as normal brightness)
ESC [ 22 m      # normal brightness

# FOREGROUND:
ESC [ 30 m      # black
ESC [ 31 m      # red
ESC [ 32 m      # green
ESC [ 33 m      # yellow
ESC [ 34 m      # blue
ESC [ 35 m      # magenta
ESC [ 36 m      # cyan
ESC [ 37 m      # white
ESC [ 39 m      # reset

# BACKGROUND
ESC [ 40 m      # black
ESC [ 41 m      # red
ESC [ 42 m      # green
ESC [ 43 m      # yellow
ESC [ 44 m      # blue
ESC [ 45 m      # magenta
ESC [ 46 m      # cyan
ESC [ 47 m      # white
ESC [ 49 m      # reset

# cursor positioning
ESC [ y;x H     # position cursor at x across, y down

# clear the screen
ESC [ mode J    # clear the screen. Only mode 2 (clear entire screen)
                # is supported. It should be easy to add other modes,
                # let me know if that would be useful."""
