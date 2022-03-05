import socket
import threading

HEADER = 64
PORT = **** #write port number to there
SERVER = socket.gethostbyname(socket.gethostname()) #auto take the ip adress
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket variable
server.bind(ADDR)


#recv message from client
def handle_client(conn, addr):
    print(f"[NEW CONNECTİON] {addr} connected.")


    connected = True

    while connected:
        
        msg = conn.recv(HEADER).decode(FORMAT)
        len_msg = len(msg)

        if len_msg != 0:
            print(msg)

            if msg == DISCONNECT_MESSAGE:
                print("connection close")
                connected = False

        else:
            print("dont recv any message from client")


    conn.close()


def start(procces_pref,input): #with procces_pref we chechk to user want to send message or recv message
    #if procces_pref is 1 this meaning user want to recv message if 2, user want to send message                                

    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    connected = True

    while connected:
        conn, addr = server.accept()

        if(input  < 255): #check message is bigger than 1 byte or not
            if procces_pref == 1: 
                handle_client(conn,addr) 

            elif procces_pref == 2:
                send_msg(conn,input)
        
        else:

            if procces_pref == 1: 
                handle_client(conn,addr)

            elif procces_pref == 2:
                send_msg_twobytes(conn,input) 

#send msg to client if input is one byte
def send_msg(conn,input):
        input = input.to_bytes(1,byteorder="big")
        conn.send(input)
        conn.flush()

#send msg to client if input is two byte
def send_msg_twobytes(conn,input):
        input = input.to_bytes(2,byteorder="big")
        conn.send(input)
        conn.flush()


thread  = threading.Thread(target = start, args = (1,200)) #rec message from client
thread.start()

thread  = threading.Thread(target = start, args = (2,200)) #send message to client (send_msg will be execute)
thread.start()

thread  = threading.Thread(target = start, args = (2,300)) #send message to client (send_msg_twobytes will be execute)
thread.start()