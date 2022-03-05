import socket
import threading
import os
import serial
import time
import logging
import os

#Create log file 

if(os.path.exists('./newfile.log') == True):
    pass


else:
    print("File created")
    # Create and configure logger
    logging.basicConfig(filename="LogFile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')


# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


#Create connection with tcp socket

HEADER = 1024
PORT = **** #manually enter port number
FORMAT = 'utf-8'
SERVER = '********'


#creat client socket variable

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    logging.debug ("socket creation failed with error %s" %(err))


try:
    #SERVER = socket.gethostbyname(socket.gethostname()) #take ip adress with this code or eter the manually 
    print (f"Server is = {SERVER}")
except socket.gaierror:

    # this means could not resolve the host
    logging.debug ("there was an error resolving the host")

# connecting to the server
try:
    client.connect((SERVER, PORT))
    #return True #if you use this code in function you can chechk to connection with return statement

except:
    logging.debug("client.connect((SERVER,PORT)) da bir sorun çıktı")

print (f"the socket has successfully connected to {SERVER}")  

#send byte message to server
sendData = 10
sendData = sendData.to_bytes(1,byteorder="big")
client.send(sendData)

#read message from server
recvData = client.recvfrom(HEADER)
print("recv data is that = ", recvData)