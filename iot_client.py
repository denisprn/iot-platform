import socket
import time
import random

HOST = '127.0.0.1'
PORT = 65432
DEVICE_ID = "sensor_001"

def generate_temperature():
    return round(random.uniform(20.0, 30.0), 2)

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")

    try:
        while True:
            temp = generate_temperature()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            message = f"{DEVICE_ID},{timestamp},{temp}"
            client.sendall(message.encode('utf-8'))
            print(f"Sent: {message}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Shutting down client...")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()