#!/usr/bin/python3

import parser

def test_parsing(fname):
  pkts = parser.parse_pcap(fname)
  for pkt in pkts:
    pkt.show()

if __name__ == "__main__":
  test_parsing("test.pcap")
