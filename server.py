import socket
import os

def start_server(host='127.0.0.1', port=65432, stop_after_one=False):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")
        
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                filename = conn.recv(1024).decode()
                print(f"Requested file: {filename}")
                
                if os.path.exists(filename):
                    with open(filename, 'r') as file:
                        contents = file.read()
                    conn.sendall(contents.encode())
                else:
                    conn.sendall(b"ERROR: File not found.")
            
            if stop_after_one:
                print("Stopping server after one interaction.")
                break

if __name__ == "__main__":
    stop_after_one = input("Stop server after one client? (y/n): ").strip().lower() == 'y'
    start_server(stop_after_one=stop_after_one)
