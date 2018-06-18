import socket
import os
import sys
from pyAudioAnalysis import audioTrainTest as aT
 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket created'

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8888

#Bind socket to Host and Port
try:
    s.bind((HOST, PORT))
except socket.error as err:
    print 'Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1]
    sys.exit()
 
print 'Socket Bind Success!'
 
 
#listen(): This method sets up and start TCP listener.
s.listen(10)
print 'Socket is now listening'
 
conn,addr = s.accept()
print 'Connet with ' + addr[0] + ':' + str(addr[1])
try:
    f = open('get_apple.wav', 'wb')
except:
    print("File Not Found!")

while 1:
    buf = conn.recv(1024)
    while(buf):
        print("Receiving...")
        f.write(buf)
        buf = conn.recv(1024)
    f.close()
    print("Receiving Done.")
    conn.send("Thank you for sending.")
    break

try:
    [Result, P, classNames] = aT.fileClassification("get_apple.wav", "svmGyungmin","svm")
    print(Result)
    print(P)
    print(classNames)
except:
    print("Can't found get_apple.wav!")

try:
    conn.send(str(Result))
    conn.send(str(P))
    conn.send(str(classNames))
except:
    print("Can't send results!")

try:
    os.remove("get_apple.wav")
except:
    print("Can't remove file!")

conn.close()
s.close() 
