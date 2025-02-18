import socket

def request_file(host='127.0.0.1', port=65432, filename=''):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(filename.encode())
        
        data = client_socket.recv(4096)  # Adjust buffer size if needed
        print("Server response:")
        print(data.decode())

if __name__ == "__main__":
    host = input("Enter server IP (default 127.0.0.1): ") or '127.0.0.1'
    port = int(input("Enter server port (default 65432): ") or 65432)
    filename = input("Enter the name of the file to request: ")
    
    request_file(host, port, filename)
