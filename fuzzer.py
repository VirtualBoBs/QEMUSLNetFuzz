#!/usr/bin/python3

import socket
import subprocess

import config

if __name__ == "__main__":
  # start target program (QEMU)
  # not implemented

  # start socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((config.HOST_IP, config.FUZZ_PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
      if config.DEBUG:
        print('Connected by', addr)
      
      while True:
        # generate file
        subprocess.run(["randpkt", "-c", str(config.PKT_SIZE), "-t", config.PKT_TYPE, "cur.pcap"])

        cur_data = b""
        with open("cur.pcap", "rb") as f:
          cur_data = f.read()

        try:
          while len(cur_data) > 0:
            conn.sendall(cur_data)

          while conn.recv(1024):
            continue
        except:
          with open("crash.pcap", "wb") as f:
            f.write(cur_data)
          break
