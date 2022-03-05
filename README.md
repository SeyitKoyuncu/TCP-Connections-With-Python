# TCP-Connections-With-Python
In this repository, i try to explain tcp socket connections like tcp server and tcp client in python. 

First of all i want to try explain files and their contents.

################# PythonTCPServer.py #################
FUNCTIONS EXPLAIN
######################################################

  start(procces_pref,input):
    In this function we have 2 function variable there are procces_pref(int) and input. With procces_pref code try to understand user want to read data from client or send message to client. If data is 1 its going to handle_client, so this meaning we want to recv message from client. On the other hand, if it is 2 this meaning is that user want to send message to client. Before there are happen this function creating requirement variables and starting so server listen.
    
  handle_client(conn, addr):
    In there, function will recv message with line 24 which is msg = conn.recv(HEADER).decode(FORMAT). Then check to the recieving message lenght if there is a nonzero, then check to message is disconnect message or not.
    
  send_msg(conn,input):
    This funciton, take connection data and input. Then convert input data to byte. And the last job is this funciton that send data and clear the buffer. 
    It is just usefull for 1 byte data.

  send_msg_twobytes(conn,input):
    This funciton same as send_msg, just have a one difference and this is that this function send 2 bytes to the client.
    
    
    
################# TcpClientPythonSide.py #############
EXPLAIN
######################################################
  In first 26 line, we set up the libraries and then search we have log file or not. If we dont have program will create then continue. 
  Between lines 31 and 34, we have neccesary variables for tcp client.
  Between lines 39 and 43, we create socket variable and check we have problem or not. If have a problem we write to the log file.
  In line 56 we connect to the server and port, with client variable.
  Between lines 65 and 67, we crate a variable and send to the server.
  Between lines 70 and 71, we read data from server and then write to date to the console.
