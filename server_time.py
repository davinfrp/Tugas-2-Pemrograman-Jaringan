from socket import *
import socket
import threading
import logging
from datetime import datetime
import sys

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                data = self.connection.recv(1024).decode('utf-8').strip()

                if data:
                    if data == "TIME":
                        now = datetime.now()
                        formatted_time = now.strftime("%H:%M:%S")
                        response = f"JAM {formatted_time}\r\n"
                        self.connection.sendall(response.encode('utf-8'))
                    elif data == "QUIT":
                        break
                    else:
                        response = "Perintah tidak dikenali.\r\n"
                        self.connection.sendall(response.encode('utf-8'))
                else:
                    break
            except Exception as e:
                logging.error(f"Error: {e}")
                break
        
        logging.warning(f"Koneksi dengan {self.address} ditutup.")
        self.connection.close()

class Server(threading.Thread):
    def __init__(self, port):
        self.the_clients = []
        self.port = port
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', self.port))
        self.my_socket.listen(1)
        logging.warning(f"Server berjalan di port {self.port}...")

        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"Koneksi baru dari {self.client_address}")
            
            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)
    
def main():
    port = 45000
    svr = Server(port)
    svr.start()

if __name__=="__main__":
    logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
    main()
