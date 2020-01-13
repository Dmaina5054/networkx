PORT=7000
HOST = ''
max_size = 1024
import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    while 1:
        print("Receiving Data")
        mesg, src = s.recvfrom(max_size)
        print(mesg)
        
if __name__ == "__main__":
    main()