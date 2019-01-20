import socket

class Listener:
    def __init__(self, host = '127.0.0.1', port = 9090, listenCnt = 1):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet, UDP
        self.sock.bind((host, port))
        print("sock binded!")
        
    def __del__(self):
        self.sock.close()
        print("sock closed!")

    def Listen(self, dataPartSize = 1024):
        allData = []
        cnt = -100
        while cnt != 0:
            data, addr = self.sock.recvfrom(dataPartSize)
            if data:
                if cnt == -100:
                    cnt = int(data)
                    self.sock.sendto("ok".encode(), addr)
                else:
                    allData.append([data, addr])
                    cnt -= 1
                    self.sock.sendto("ok".encode(), addr)
        print(allData)
    

print("start")
listener = Listener()
listener.Listen()
print("end")