import socket
import test_pb2
import time
import random

tst = test_pb2.test()
tst.counter = 0
port = 8900
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while tst.counter < 2500:
    tst.brake = random.uniform(1, 10)
    tst.counter += 1
    str = tst.SerializeToString()
    print(tst.brake)
    udp_socket.sendto(str, ("192.168.31.235", port))
    time.sleep(0.0001)
