import socket
from tqdm import tqdm
import logging

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)


def main():
    """ Creating a TCP server socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    logging.info("Listening...")

    """ Accepting the connection from the client. """
    conn, addr = server.accept()
    logging.info(f"Client connected from {addr[0]}:{addr[1]}")

    """ Receiving the filename and file_size from the client. """
    data = conn.recv(SIZE).decode(FORMAT)
    item = data.split("_")
    filename = item[0]
    file_size = int(item[1])

    logging.info("Filename and file_size received from the client.")
    conn.send("Filename and file_size received".encode(FORMAT))

    """ Data transfer """
    bar = tqdm(range(file_size), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(f"recv_{filename}", "wb") as f:
        while True:
            data = conn.recv(SIZE)

            if not data:
                break

            f.write(data)
            conn.send("Data received.".encode(FORMAT))

            bar.update(len(data))

    """ Closing connection. """
    conn.close()
    server.close()


if __name__ == "__main__":
    main()

