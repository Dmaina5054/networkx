

import time
import random

import socket
import os
host = '192.168.1.191'

PORT = random.randint(7000,10000)
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, PORT))
    print("Listening on {}".format(PORT))
    s.listen(5)
    print("Listening for client connections")
    while 1:
        conn, addr = s.accept()
        print(addr)
        
        import os
        os.system('dig -x {} | grep PTR'.format(addr[0]))
     
        print("Same Subnet")
        
        print("TRANSACTION: {}\n".format(time.ctime()))
        
        

    
if __name__ == '__main__':
    main()
    