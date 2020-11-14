import socket, struct

def SendString(s, str):
    n = len(str)
    s.send(struct.pack(f'i{n}s', n, str.encode('cp866')))

def ReceiveString(s):
    n = struct.unpack('i', s.recv(4))[0]
    return struct.unpack(f'{n}s', s.recv(n))[0].decode('cp866')


HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        SendString(s, input())
        print(ReceiveString(s))
