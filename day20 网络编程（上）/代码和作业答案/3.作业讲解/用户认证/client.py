# socket服务端（接收者）
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(5)
conn, addr = sock.accept()

client_data = conn.recv(1024)
print(client_data.decode('utf-8'))

conn.close()
sock.close(
