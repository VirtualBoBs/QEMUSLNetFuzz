#!/usr/bin/python3

import pyshark

def parse_pcap(filename):
  pkts = pyshark.FileCapture(input_file=filename)
  return pkts



