PORT = 10000
MAX_SIZE = 1024

import socket
import time

def main():
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('',PORT))

    while 1:
       # mesg= input('Enter 2 send here: \n')
      #  if len(mesg) > 0:
        s.send(time.ctime())
        
if __name__ == '__main__':
    main()
