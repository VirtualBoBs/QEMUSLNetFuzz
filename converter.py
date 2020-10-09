#!/usr/bin/python3

from scapy.all import *

def ip_vec_to_pkt(vec):
  print(vec)
  return IP(ihl=vec[0], tos=vec[1], len=vec[2], id=vec[3], flags=vec[4], frag=vec[5], \
    ttl=vec[6], proto=vec[7])/vec[8]