import socket

target = input("Enter IP address: ")

for port in range(20, 100):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = s.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is open")

    s.close()