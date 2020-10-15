#!/usr/bin/python3

import socket
import subprocess

import config

if __name__ == "__main__":
  # start target program (QEMU)
  # not implemented

  # start socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", config.FUZZ_PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
      if config.DEBUG:
        print('Connected by', addr)
      
      while True:
        if config.DEBUG:
          print("running file")

        # generate file
        subprocess.run(["randpkt", "-c", str(config.PKT_SIZE), "-b", str(config.MTU), "-t", config.PKT_TYPE, "cur.pcap"])

        cur_data = b""
        with open("cur.pcap", "rb") as f:
          cur_data = f.read()

        if config.DEBUG:
          print("file length :", len(cur_data))

        try:
          if len(cur_data) % 1024 != 0:
            conn.sendall(cur_data)
          else:
            conn.sendall(cur_data + b"over")

          if config.DEBUG:
            print("Sending file done")

          if conn.recv(1024):
            continue
        except KeyboardInterrupt:
          break
        except:
          with open("crash.pcap", "wb") as f:
            f.write(cur_data)
          break
