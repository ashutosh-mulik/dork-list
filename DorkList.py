import webbrowser
import platform
import sys

data = open("dork.txt",encoding="utf8")
dorks = []
a = """▓█████▄  ▒█████   ██▀███   ██ ▄█▀    ██▓     ██▓  ██████ ▄▄▄█████▓
▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒    ▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒
░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░    ▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░
░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄    ▒██░    ░██░  ▒   ██▒░ ▓██▓ ░ 
░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄   ░██████▒░██░▒██████▒▒  ▒██▒ ░ 
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   
 ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░   ░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░    
 ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░      ░ ░    ▒ ░░  ░  ░    ░      
   ░        ░ ░     ░     ░  ░          ░  ░ ░        ░           
 ░                                                                """

print(a)

def getMac():
    # MacOS
    return 'open -a /Applications/Google\ Chrome.app %s'

def getWindows():
    # Windows
    if platform.architecture()[0] == "32bit":
        return 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    
    if platform.architecture()[0] == "64bit":
        return 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def getLinux():
    # Linux
    return '/usr/bin/google-chrome %s'

def showList():
    count = 1
    for line in data:
        print("{:02d}".format(count),line,end="")
        dorks.append(line)
        count += 1

def getInput():
    inp = 0
    try:
        inp = int(input("\n\nEnter Dork Number : ")) - 1
    except:
        print("invalid Input.")
    return inp

def showResult(i):
    url = 'https://www.google.com/search?q=' + dorks[i]
    print("Showing result for :",dorks[i])
    if sys.platform == "linux" or sys.platform == "linux2":
        # linux
        webbrowser.get(getLinux()).open(url)
    elif sys.platform == "darwin":
        # OS X
        webbrowser.get(getMac()).open(url)
    elif sys.platform == "win32":
        # Windows...
        webbrowser.get(getWindows()).open(url)

showList()

a = 1
while a:
    showResult(getInput())
    a = int(input("Enter 1 to continue : "))
