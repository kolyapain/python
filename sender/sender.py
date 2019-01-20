import socket

class Sender:
    def __init__(self, ip = '127.0.0.1', port = 9090):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((ip, port))
        print("sock connected")

    def __del__(self):
        self.sock.close()
        print("sock closed")

    def SendMsg(self, msgList):
        self.sock.sendto(str(len(msgList)).encode(), (self.ip, self.port))
        answer, addr = self.sock.recvfrom(1024)
        print(answer)
        for msg in msgList:
            self.sock.sendto(msg.encode('UTF-8'), (self.ip, self.port))
            answer, addr = self.sock.recvfrom(1024)
            print(answer, addr)

sender = Sender()
msgs = ["this", "is", "a","test","message"]
sender.SendMsg(msgs)
