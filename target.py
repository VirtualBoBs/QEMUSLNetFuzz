#!/usr/bin/python3
  
import socket
import pyshark
import nest_asyncio

import config
import parser

if __name__ == "__main__":
  # pyshark async problem resolve
  nest_asyncio.apply()

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.connect((config.HOST_IP, config.FUZZ_PORT))

    # recv pcap data
    while True:
      pcap_data = b""
      while True:
        data = conn.recv(1024)
        if not data:
          break
        
        # if len(data) % 1024 == 0
        if data == b"over":
          break

        pcap_data += data

        if len(data) != 1024:
          break
      
      if config.DEBUG:
        print("pcap len :", len(pcap_data))

      # save file and parse it
      with open("rcv.pcap", "wb") as f:
        f.write(pcap_data)
      pkts = parser.parse_pcap("rcv.pcap")

      if config.DEBUG:
        pkts.set_debug()

      raw_sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
      raw_sock.bind((config.INTERFACE_NAME, 0))

      for pkt in pkts:
        raw_sock.send(bytearray.fromhex(pkt.frame_raw.value))
      pkts.close()

      conn.sendall(b"NXT")
