import requests
import time
import sys

host = sys.argv[1];
command=""
for i in range(3, len(sys.argv)):
    command = command+" "+sys.argv[i]

directory = sys.argv[2];
print command
print host
print directory
if True:
    try:
        r = requests.post(host, data={'command': command, "directory":directory})
        print(r.status_code, r.reason)
        print r.text;
    except Exception as e:
        print e

