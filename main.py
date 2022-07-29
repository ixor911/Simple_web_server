from socket import *


def create_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while True:
            (client_socket, address) = server_socket.accept()

            request = client_socket.recv(5000).decode()
            pieces = request.split(' ')
            if len(pieces) > 0: print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n" \
                   "Connection-Type: text/html; charset=utf=8\r\n" \
                   "\r\n" \
                   "<html><body>Hello world</body></html>"
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exp:
        print("ERROR: \n")
        print(exp)

    server_socket.close()


print("Access http://localhost:9000")
create_server()
