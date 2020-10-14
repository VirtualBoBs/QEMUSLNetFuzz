#!/usr/bin/python3

import socket
import pyshark

import config
import parser

if __name__ == "__main__":
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.connect((config.HOST_IP, config.FUZZ_PORT))
    
    # recv pcap data
    pcap_data = b""
    while True:
      data = conn.recv(1024)
      if not data or len(data) != 1024:
        break
      else:
        pcap_data += data
    
      # save file and parse it
      with open("rcv.pcap", "wb") as f:
        f.write(pcap_data)
      pkts = parser.parse_pcap("rcv.pcap")
  
      raw_sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
      raw_sock.bind((config.INTERFACE_NAME, 0))
  
      for pkt in pkts:
        raw_sock.send(bytearray.fromhex(pkt.frame_raw.value))
      pkts.close()
      
      conn.sendall("NXT")

