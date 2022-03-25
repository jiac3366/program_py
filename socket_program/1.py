import logging
import socket

from select import select
from threading import Thread
from multiprocessing import Queue
from multiprocessing import Process
from sys import stdout
from time import sleep


class ServerApp(object):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(stdout)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


    def conn_handler(self, connection, address, buffer):

        self.logger.info("[%d] - Connection from %s:%d", self.id, address[0], address[1])

        try:
            while True:

                command = None
                received_data = b''
                readable, writable, exceptional = select([connection], [], [], 0)  # Check for client commands

                if readable:
                    # Get Command  ... There is more code here
                    command = 'Something'


                if command == 'Something':
                    connection.sendall(command_response)
                else:
                    print(':(')

        except Exception as e:
            print(e)
        finally:
            connection.close()
            self.client_buffers.remove(buffer)
            self.logger.info("[%d] - Connection from %s:%d has been closed.", self.id, address[0], address[1])


    def join(self):

        while self.listener.is_alive():
            self.listener.join(0.5)


    def acceptor(self):

        while True:
            self.logger.info("[%d] - Waiting for connection on %s:%d", self.id, self.ip, self.port)

            # Accept a connection on the bound socket and fork a child process to handle it.
            conn, address = self.socket.accept()

            # Create Queue which will represent buffer for specific client and add it o list of all client buffers
            buffer = Queue()
            self.client_buffers.append(buffer)

            process = Process(target=self.conn_handler, args=(conn, address, buffer))
            process.daemon = True
            process.start()
            self.clients.append(process)

            # Close the connection fd in the parent, since the child process has its own reference.
            conn.close()


    def __init__(self, id, port=4545, ip='127.0.0.1', method='tcp', buffer_size=2048):

        self.id = id
        self.port = port
        self.ip = ip

        self.socket = None
        self.listener = None
        self.buffer_size = buffer_size

        # Additional attributes here....

        self.clients = []
        self.client_buffers = []


    def run(self):

        # Create TCP socket, bind port and listen for incoming connections
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))
        self.socket.listen(5)


if __name__ == '__main__':
    socket.socketpair()