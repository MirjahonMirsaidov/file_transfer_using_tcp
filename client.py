import logging
import os
import socket
from tqdm import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
FILENAME = "scene.jpg"
FILESIZE = os.path.getsize(FILENAME)

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)


def main():
    """ TCP socket and connecting to the server """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    """ Sending the filename and filesize to the server. """
    data = f"{FILENAME}_{FILESIZE}"
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    logging.info(f"SERVER: {msg}")

    """ Data transfer. """
    bar = tqdm(range(FILESIZE), f"Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(FILENAME, "rb") as f:
        while True:
            data = f.read(SIZE)

            if not data:
                break

            client.send(data)
            client.recv(SIZE).decode(FORMAT)

            bar.update(len(data))

    """ Closing the connection """
    client.close()


if __name__ == "__main__":
    main()
