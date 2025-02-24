import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

sensor_data = []

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received from {addr}: {data}")
            sensor_data.append(data)
        except ConnectionResetError:
            break
    print(f"Connection from {addr} closed")
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()