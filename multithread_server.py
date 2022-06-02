import logging
import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)


def handle_client(conn, addr):
    logging.info(f"Client connected from {addr[0]}:{addr[1]}")

    """ Receiving the filename and filesize from the client. """
    data = conn.recv(SIZE).decode(FORMAT)
    item = data.split("_")
    filename = item[0]

    logging.info("Filename and filesize received from the client.")
    conn.send("Filename and filesize received".encode(FORMAT))

    """ Data transfer """
    with open(f"recv_{filename}", "wb") as f:
        while True:
            data = conn.recv(SIZE)

            if not data:
                break

            f.write(data)
            conn.send("Data received.".encode(FORMAT))
    logging.info(f"File <{filename}> succesfully transfered")
    """ Closing connection. """
    conn.close()


def main():
    logging.info("Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    logging.info(f"Server is listening on {IP}:{PORT}.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        logging.info(f"ACTIVE CONNECTIONS {threading.active_count() - 1}")


if __name__ == "__main__":
    main()

