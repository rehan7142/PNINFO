import subprocess
import os

os.system("clear")

## Color code ##
Y = "\033[93m"
G = "\033[32m"
B = "\033[41m"
D = "\033[49m"
### ### ##### ####

def menu():
    print G+ " _   _  ____           _____ ___   ___  _ "
    print G+ "| \ | |/ ___|         |_   _/ _ \ / _ \| | "
    print G+ "|  \| | |      _____    | || | | | | | | | "
    print G+ "| |\  | |___  |_____|   | || |_| | |_| | |___ "
    print G+ "|_| \_|\____|           |_| \___/ \___/|_____| "
    print''
    print Y+ ("[*] TOOL CREATED BY NALLA-CODER [*]")
    print G+ ('')
    d = ("truecallerjs -s ")
    num = raw_input("[*] ENTER MOBILE NO WITH COUNTRY CODE WITHOUT (+) : ")
    lm = (d + num)
    subprocess.call(lm , shell=True)
    print''
    k = raw_input("[*] Press enter to continue [*]")
    if k == "":
        os.system("clear")
        menu()
    else:
        os.system("clear")
        menu()
    
    
print(menu())
