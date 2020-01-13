PORT= 10000

import socket

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    DEST = ''
   # DEST = str(input("Enter destination ip\n"))

    while True:
        mesg = (input("enter message text now:\n"))
        if len(mesg) > 0:
            s.sendto(b'mesg',(DEST,PORT))
if __name__ == "__main__":
    main()