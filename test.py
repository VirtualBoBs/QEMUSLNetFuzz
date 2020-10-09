#!/usr/bin/python3

from scapy.all import *

import generator

if __name__ == "__main__":
  generator.gen_pkt().show()