#!/usr/bin/python3

import pyshark

def parse_pcap(filename):
  pkts = pyshark.FileCapture(input_file=filename, use_json=True, include_raw=True)#._packets_from_tshark_sync()
  return pkts



